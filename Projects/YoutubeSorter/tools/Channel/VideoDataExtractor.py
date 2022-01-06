import json
import os

from tqdm import tqdm


def extract(youtube, pl_id):
    if os.path.exists("VideoDataChannel.json"):
        with open("VideoDataChannel.json") as file:
            return json.load(file)

    next_page_token = None
    data = {}
    page_no = 0
    vids = []

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
        for video in pl_response["items"]:
            vid = video["contentDetails"]["videoId"]

            vid_ids.append(vid)
            vids.append(vid)
        print("Fetched Video ID's")

        for vid_id in tqdm(vid_ids):
            vid_response = youtube.videos().list(
                part="snippet",
                id=vid_id,
            ).execute()

            vid_snippet = vid_response["items"][0]["snippet"]
            channel_id = vid_snippet["channelId"]

            if (channel_id not in data.keys()):
                data[channel_id] = {"name": vid_snippet["channelTitle"]}

            if ("videos" in data[channel_id].keys()):
                data[channel_id]["videos"].append(vid_id)
            else:
                data[channel_id]["videos"] = []
                data[channel_id]["videos"].append(vid_id)

        page_no += 1
        print(f"\nNext Page ({page_no})")
        next_page_token = pl_response.get("nextPageToken")

        if not next_page_token:
            break

    with open("VideoDataChannel.json", "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Wrote Data to File")

        print("\nFinished Extracting")
        print(f"\nTotal No. of Videos: {len(vids)}\n\n")

        return data
