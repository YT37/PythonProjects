import json

from tqdm import tqdm

from tools import Service, VideoDataExtractor

# TODO: Change These
pl_id = "PLzAHI18MJ6GRXuairTpiSQOk1Rp1u9Ytf"
secret_file = "Secret.json"


def main():
    print("Starting\n\n")

    youtube = Service.create(secret_file)
    video_data = VideoDataExtractor.extract(youtube, pl_id)

    try:
        pl_response = youtube.playlists().insert(
            part="snippet",
            body={
                "snippet": {
                    "title": "List"
                },
            },
        ).execute()

        new_pl_id = pl_response["id"]

        for video in tqdm(list(video_data.keys())):
            pl_response = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": new_pl_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video,
                        },
                    },
                },
            ).execute()

            video_data.pop(video)
            with open("VideoData.json", "w") as file:
                file.write(json.dumps(video_data, indent=4))

    except:
        print(
            "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
        )

    finally:
        print("Finished")


if __name__ == "__main__":
    if (pl_id and secret_file) != "":
        main()
    else:
        print(
            "Please specify your Channel ID, Playlist ID & Secret File location."
        )
