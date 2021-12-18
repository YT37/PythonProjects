import json
import os

import isodate
from tqdm import tqdm


def extract(youtube, pl_id):
    if os.path.exists("VideoData.json"):
        with open("VideoData.json") as file:
            return json.load(file)

    next_page_token = None
    data = {}
    page_no = 0

    print("Starting Extracting")
    while True:
        pl_response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=pl_id,
            maxResults=50,
            pageToken=next_page_token,
        ).execute()
        print("Fetched Playlist")

        vid_ids = []
        for vid in pl_response["items"]:
            vid_ids.append(vid["contentDetails"]["videoId"])
        print("Fetched Video ID's")

        for vid_id in tqdm(vid_ids):
            vid_response = youtube.videos().list(
                part="contentDetails",
                id=vid_id,
            ).execute()

            vid_details = vid_response["items"][0]["contentDetails"]
            duration = (isodate.parse_duration(
                vid_details["duration"])).total_seconds()

            data[vid_id] = duration

        page_no += 1
        print(f"\nNext Page ({page_no})")
        next_page_token = pl_response.get("nextPageToken")

        data = dict(sorted(data.items(), key=lambda item: item[1]))

        if not next_page_token:
            break

    with open("VideoData.json", "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Wrote Data to File")

        print("\nFinished Extracting")
        print(f"\nTotal No. of Videos: {len(data.keys())}\n\n")

        return data
