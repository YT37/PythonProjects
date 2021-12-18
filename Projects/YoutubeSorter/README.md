# YoutubeSorter
- This project extracts all the data from the videos in a YT Playlists & Sorts them according to Channel or Duration.

# Requirements
- Python 3.6 or up
- Google OAuth Lib
- Google API
- ISODate
- TQDM

# Instructions
- Make Project in Google Cloud
- Add Youtube Data V3 API
- Configure OAuth 2.0 Consent Screen and Publish it to Production
- Place the Credentials file in the folder
- Make sure to change Channel ID, Playlist ID & Secret File Path in YoutubeSorter.py (Lines: 4-6)

- **Windows, Mac and Linux**
  ``` 
  pip install -r requirements.txt
  ```
- **Windows**
  ```
  python YoutubeSorter.py
  ```
- **Mac or Linux**
  ```
  python3 YoutubeSorter.py
  ```
