import json

from tqdm import tqdm

from . import PlaylistDataExtractor, VideoDataExtractor


def sort(youtube, channel_id, pl_id):
    video_data = VideoDataExtractor.extract(youtube, pl_id)
    playlists_data = PlaylistDataExtractor.extract(youtube, channel_id)

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

            except Exception as e:
                if e.args[0]["status"] == "403":
                    print(
                        "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
                    )
                else:
                    print(e)

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

            except Exception as e:

                video_data[
                    channel_data[0]]["videos"] = videos[videos.index(vid_id):]

                with open("VideoData.json", "w") as file:
                    file.write(json.dumps(video_data, indent=4))

                if e.args[0]["status"] == "403":
                    print(
                        "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
                    )
                else:
                    print(e)

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
