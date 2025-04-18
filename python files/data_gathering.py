###############################################################################
# Script Name:     data_gathering.py
# Author:          Q.A. Boahene
# Description:     Getting the lyrics from the discographies of 10 musicians
#                  spanning different genres. This is supposed to use spotify
#                  album listings to get song names and then get the lyrics for
#                  the song from the Genius API but using lyrics links and then
#                  scraping the lyrics from the webpages.
# Created On:      2025-04-18
# Version:         1.0.0
# License:         MIT
###############################################################################

# Importing needed modules
import os
import json
import pandas as pd
import lyricsgenius
from genius_config import ACCESS_TOKEN
from lyricsgenius import Genius as gn


genius = gn(ACCESS_TOKEN, sleep_time=0.2, timeout=10, retries=0)


def get_artist_id(artist_name):
    artist_search = genius.search_artist(artist_name, max_songs=0)
    return artist_search.id


def get_artist_album_list(artist_id):
    artist_albums_info_dict = genius.artist_albums(artist_id, per_page=50)
    # trimmed_album_info = [artist_albums_info_dict['albums']]
    albums_info = [
        (album["name"], album["id"]) for album in artist_albums_info_dict["albums"]
    ]
    return albums_info


def get_album_lyrics(album_id_list, artist_name, destination):
    create_album_folder = os.path.join(destination, artist_name)

    check_folder = os.path.isdir(create_album_folder)
    if not check_folder:
        os.makedirs(create_album_folder)
        print("Created a folder for : ", artist_name)
    else:
        print(artist_name, "already has a folder in this directory!")

    for i in album_id_list:
        album_name = i[0]
        album_search = genius.search_album(album_name, artist_name)
        album_info_json = album_search.to_json()
        album_info = json.loads(album_info_json)
        album_data = pd.json_normalize(album_info, record_path=["tracks"])
        album_data = album_data[
            ["song.artist", "song.title", "song.title_with_featured", "song.lyrics"]
        ]
        album_data = album_data.rename(
            columns={
                "song.artist": "artist_name",
                "song.title": "song_title",
                "song.title_with_featured": "title_with_featured",
                "song.lyrics": "song_lyrics",
            }
        )
        album_data.to_csv(os.path.join(create_album_folder, album_name + ".csv"))
    return ()


# get last played tracks
artist_to_search = input("Well, which musician are we looking into today?: ")
artist_id = get_artist_id(artist_to_search)
# print(artist_id)

artist_albums = get_artist_album_list(artist_id)
# print(artist_albums)
print(
    "\nHere are the album(s) and mixtape(s) by "
    + artist_to_search
    + " with lyrics on genius.com"
)
for index, track in enumerate(artist_albums):
    print(f"{index + 1} - {track[0]}")

# choose which albums to download lyrics of
indexes = input(
    "\nEnter a list of albums tracks you'd like to download. Use indexes separated by a space: "
)
indexes = indexes.split()
chosen_albums = [artist_albums[int(index) - 1] for index in indexes]
# print(chosen_albums)

albums_folder = input(
    "\nEnter the link to the folder which you want the selected album lyrics to be downloaded: "
)
get_album_lyrics(chosen_albums, artist_to_search, albums_folder)
