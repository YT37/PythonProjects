import json
import os

from tqdm import tqdm

from Tools import PlaylistExtractor, Service


def main():
    print("Starting")

    # TODO: Change These
    pl_id = ""
    secret_file = ""

    youtube = Service.create(secret_file)
    data = {}

    if not os.path.exists("PlaylistData.json"):
        PlaylistExtractor.get_data(youtube, pl_id)

    with open("PlaylistData.json") as file:
        data = json.load(file)

    for channel_data in tqdm(data.items()):
        pl_response = youtube.playlists().insert(
            part="snippet",
            body={
                "snippet": {
                    "title": channel_data[1]["name"]
                },
            },
        ).execute()
        pl_id = pl_response["id"]

        for vid_id in channel_data[1]["videos"]:
            pl_response = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": pl_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": vid_id,
                        },
                    },
                },
            ).execute()

    print("Finished")


if __name__ == "__main__":
    main()
