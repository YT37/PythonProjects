import os
import subprocess
from sys import platform

import requests
from bs4 import BeautifulSoup

# TODO: Change These Paths
plexTV = "/mnt/STORAGE/Plex/TV Shows"
plexMovies = "/mnt/STORAGE/Plex/Movies"

try:
    type = input(
        "What do you want to import to Plex? (1. TV Show, 2. Movie): ",
    ).lower().strip()

    if type == "tv show" or type == "show" or type == "1":
        link = input(
            "Enter TVDB Link (Ex: https://www.thetvdb.com/series/(series-id)): "
        )
        info = BeautifulSoup(requests.get(link).text, "lxml")

        id = info.findChild(
            class_="list-group-item clearfix").text.split("\n")[2].strip()

        title = info.findChild(id="series_title").text.strip()
        year = info.findChildren(class_="list-group-item-text")[-1].text.strip(
        ).split(" ")[1].strip()

        season = int(input("Enter Season No.: "))

        episodeInfo = BeautifulSoup(
            requests.get(f"{link}/seasons/official/{season}").text,
            "lxml",
        )
        episodes = [
            title.text.strip() for headlines in episodeInfo.find_all("td")
            for title in headlines.find_all("a")
        ]

        showPath = f"{plexTV}/{title} ({year}) {{tvdb-{id}}}/Season {season}/"

        if not os.path.exists(showPath): os.makedirs(showPath)
        os.chdir(showPath)

        files = os.listdir()

        if platform == "linux" or platform == "linux2":
            subprocess.Popen(["xdg-open", showPath])
        elif platform == "darwin":
            subprocess.Popen(["open", showPath])
        elif platform == "win32":
            subprocess.Popen(f"explorer '{showPath}'")

        input(f"Move the files in opened location and press a key. ")

        for index in range(len(files)):
            files.sort()

            os.rename(
                files[index],
                f"{title} ({year}) S{season:02}E{index+1:02} - {episodes[index]}.{files[index].split('.')[-1]}",
            )

        print(f"\nImported {len(files)} Files Successfully")

    elif type == "movie" or type == "2":
        link = input(
            "Enter TVDB Link (Ex: https://www.thetvdb.com/movies/(movie-id)): "
        )
        info = BeautifulSoup(requests.get(link).text, "lxml")

        id = info.findChild(
            class_="list-group-item clearfix").text.split("\n")[2].strip()

        title = info.findChild(id="series_title").text.strip()
        year = info.findChildren(
            class_="list-group-item clearfix")[2].text.strip().split(
                "\n")[3].split(",")[1].strip()

        moviePath = f"{plexMovies}/{title} ({year}) {{tvdb-{id}}}/"

        if not os.path.exists(moviePath): os.makedirs(moviePath)
        os.chdir(moviePath)

        files = os.listdir()

        if platform == "linux" or platform == "linux2":
            subprocess.Popen(["xdg-open", moviePath])
        elif platform == "darwin":
            subprocess.Popen(["open", moviePath])
        elif platform == "win32":
            subprocess.Popen(f"explorer '{moviePath}'")

        input(f"Move the files in opened location and press a key. ")

        file = os.listdir()[0]
        os.rename(
            file,
            f"{title} ({year}).{file.split('.')[-1]}",
        )

        print(f"\nImported 1 Files Successfully")

    else:
        print("Please enter a valid input.")
        exit()

except Exception as e:
    print(f"An Error Occurred: {e}")
