# YoutubePlaylistDurationSorter
- This project extracts all the data from the videos in YT Playlists & Sorts them according to Duration.
- Limited to 200 Videos
- Creates new Playlist if Creds are Changed.

# Requirements
- Python 3.6 or up
- Google API
- Google OAuth Lib
- TQDM
- ISODate

# Instructions
- Make Project in Google Cloud
- Add Youtube Data V3 API
- Configure OAuth 2.0 Consent Screen and Publish it to Production
- Place the Credentials file in the folder
- Make sure to change Channel ID & Secret File Path in YoutubePlaylistDurationSorter.py (Lines: 9-11)

- **Windows, Mac and Linux**
  ``` 
  pip install -r requirements.txt
  ```
- **Windows**
  ```
  python YoutubePlaylistDurationSorter.py
  ```
- **Mac or Linux**
  ```
  python3 YoutubePlaylistDurationSorter.py
  ```
