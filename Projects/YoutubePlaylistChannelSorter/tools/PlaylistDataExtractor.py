import json


def extract(youtube, channel_id):
    nextPageToken = None
    data = {}
    pageNo = 0

    print("Starting Extracting")
    while True:
        channel_response = youtube.playlists().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=nextPageToken,
        ).execute()
        print("Fetched Playlists")

        for playlist_data in channel_response["items"]:
            data[playlist_data["snippet"]["localized"]
                 ["title"]] = playlist_data["id"]

        pageNo += 1
        print(f"Next Page ({pageNo})")
        nextPageToken = channel_response.get('nextPageToken')

        if not nextPageToken:
            break

    with open("PlaylistData.json", "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Wrote Data to File")

    print("Finished Extracting")
