import json
import os

from tqdm import tqdm

from tools import PlaylistDataExtractor, Service, VideoDataExtractor

# TODO: Change These
channel_id = ""
pl_id = ""
secret_file = ""


def main():
    print("Starting")

    youtube = Service.create(secret_file)
    video_data = {}
    playlists_data = {}

    if not os.path.exists("PlaylistData.json"):
        PlaylistDataExtractor.extract(youtube, channel_id)

    with open("PlaylistData.json") as file:
        playlists_data = json.load(file)

    if not os.path.exists("VideoData.json"):
        VideoDataExtractor.extract(youtube, pl_id)

    with open("VideoData.json") as file:
        video_data = json.load(file)

    for channel_data in tqdm(list(video_data.items())):
        title = channel_data[1]["name"]
        videos = channel_data[1]["videos"]

        if title not in playlists_data:
            try:
                pl_response = youtube.playlists().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "title": title
                        },
                    },
                ).execute()

                new_pl_id = pl_response["id"]
                playlists_data[title] = new_pl_id

            except:
                print(
                    "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
                )
                break

        else:
            new_pl_id = playlists_data[title]

        for vid_id in videos:
            try:
                pl_response = youtube.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": new_pl_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": vid_id,
                            },
                        },
                    },
                ).execute()

            except:
                video_data[
                    channel_data[0]]["videos"] = videos[videos.index(vid_id):]

                with open("VideoData.json", "w") as file:
                    file.write(json.dumps(video_data, indent=4))

                print(
                    "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
                )
                break

            finally:
                with open("PlaylistData.json", "w") as file:
                    file.write(json.dumps(playlists_data, indent=4))

        else:
            video_data.pop(channel_data[0])
            with open("VideoData.json", "w") as file:
                file.write(json.dumps(video_data, indent=4))

            continue

        break

    print("Finished")


if __name__ == "__main__":
    if (channel_id and pl_id and secret_file) != "":
        main()
    else:
        print(
            "Please specify your Channel ID, Playlist ID & Secret File location."
        )
