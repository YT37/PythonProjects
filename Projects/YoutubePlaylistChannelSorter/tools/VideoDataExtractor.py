import json

from tqdm import tqdm


def extract(youtube, pl_id):
    nextPageToken = None
    data = {}
    pageNo = 0

    print("Starting Extracting")
    while True:
        pl_response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=pl_id,
            maxResults=50,
            pageToken=nextPageToken,
        ).execute()
        print("Fetched Playlist")

        vid_ids = []
        for vid in pl_response["items"]:
            vid_ids.append(vid["contentDetails"]["videoId"])
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

        pageNo += 1
        print(f"Next Page ({pageNo})")
        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break

    with open("VideoData.json", "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Wrote Data to File")

    print("Finished Extracting")
