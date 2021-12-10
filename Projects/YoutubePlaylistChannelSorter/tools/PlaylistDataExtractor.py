import json
import os


def extract(youtube, channel_id):
    if os.path.exists("PlaylistData.json"):
        with open("PlaylistData.json") as file:
            return json.load(file)

    next_page_token = None
    data = {}
    page_no = 0
    video_count = 0

    print("Starting Extracting")
    while True:
        channel_response = youtube.playlists().list(
            part="snippet, contentDetails",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
        ).execute()
        print("Fetched Playlists")

        for playlist_data in channel_response["items"]:
            video_count += playlist_data["contentDetails"]["itemCount"]
            data[playlist_data["snippet"]["localized"]
                 ["title"]] = playlist_data["id"]

        page_no += 1
        print(f"\nNext Page ({page_no})")
        next_page_token = channel_response.get("nextPageToken")

        if not next_page_token:
            break

    with open("PlaylistData.json", "w") as file:
        file.write(json.dumps(data, indent=4))
        print("Wrote Data to File")

        print("\nFinished Extracting")
        print(f"\nTotal No. of Videos: {video_count}\n")

        return data
