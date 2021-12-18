import json
import os
from hashlib import new

from tqdm import tqdm

from .. import Service
from . import VideoDataExtractor


def sort(youtube, pl_id):
    video_data = VideoDataExtractor.extract(youtube, pl_id)

    new_pl_id = ""
    use_old_pl = False

    if os.path.exists("PlaylistData.json"):
        old_pl_data = {}
        with open("PlaylistData.json") as file:
            old_pl_data = json.load(file)

        new_pl_id = old_pl_data["id"]
        input_old_pl = input(
            f"Do you want to use the:\n1. Old Playlist ({new_pl_id}) \n2. New Playlist\n\n"
        )

        if input_old_pl == "1" or input_old_pl == "old" or input_old_pl == "Old Playlist" or input_old_pl == new_pl_id:
            use_old_pl = True
        elif input_old_pl == "2" or input_old_pl == "new" or input_old_pl == "New Playlist":
            use_old_pl = False
        else:
            print("Please enter the correct input.")
            return

    try:
        if not use_old_pl:
            pl_response = youtube.playlists().insert(
                part="snippet",
                body={
                    "snippet": {
                        "title": "List"
                    },
                },
            ).execute()

            new_pl_id = pl_response["id"]

            with open("PlaylistData.json", "w") as file:
                file.write(json.dumps(pl_response, indent=4))

        for video in tqdm(list(video_data.keys())):
            print(video)
            youtube.playlistItems().insert(
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

    except Exception as e:
        if e.args[0]["status"] == "403":
            print(
                "The API quota has exceeded. Please try after 24 Hrs or Create a new project (Delete Token.pickle)"
            )
        else:
            print(e)