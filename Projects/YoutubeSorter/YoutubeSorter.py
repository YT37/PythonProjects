import os

from tools import Channel, Duration, Service

# TODO: Change These
channel_id = ""
pl_id = ""
secret_file = ""


def main():
    print("Starting\n\n")

    youtube = Service.create(secret_file)
    channel_sort = False

    sort_type = input(
        "Do you want to sort the Playlist by:\n1. Channel\n2. Duration\n\n"
    ).lower()

    if sort_type == "1" or sort_type == "channel":
        channel_sort = True
    elif sort_type == "2" or sort_type == "duration":
        channel_sort = False
    else:
        print("Please enter the correct input.")
        return

    if channel_sort:
        Channel.sort(youtube, channel_id, pl_id)
        with open("VideoDataChannel.json") as file:
            if file.read() == "{}":
                os.remove("VideoDataChannel.json")
                os.remove("PlaylistData.json")
    else:
        Duration.sort(youtube, pl_id)

        with open("VideoDataDuration.json") as file:
            if file.read() == "{}":
                os.remove("VideoDataDuration.json")
                os.remove("PlaylistData.json")

    print("Finished")


if __name__ == "__main__":
    if (channel_id and pl_id and secret_file) != "":
        main()
    else:
        print(
            "Please specify your Channel ID, Playlist ID & Secret File location."
        )
