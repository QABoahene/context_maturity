# Needed modules
import pandas as pd
import os

# Data Preparation function

## List album folders there
def list_artists(artists_folder_link):
    directory_list = [item for item in os.listdir(artists_folder_link) if os.path.isdir(os.path.join(artists_folder_link, item))]
    return (directory_list)

## Ask where album folder is
albums_folder = input("\nEnter folder link to where the artist folders are: ")
artist_list = list_artists(albums_folder)
print("\nHere are the artist(s) in the link provided")
for index, artist in enumerate(artist_list):
    print(f"{index+1} - {artist}")

# choose which artist to get lyrics data from
indexes = input("\nEnter the index of the artist you want: ")
chosen_artist = [artist_list[int(index)-1] for index in indexes]
print("\nYou chose " + chosen_artist[0] + ", lets get their data for you!")



## Select artist
## Import the data  
## Add album name column
## combine all album songs
### That is the data to be cleaned
# /Users/qaboahene/Desktop/Albums_Folder