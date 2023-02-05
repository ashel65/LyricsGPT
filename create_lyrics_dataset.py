import json, os
from datasets import load_dataset

# To create a dataset suitable for training, I need to grab only the lyrics of each
# song from each artist's JSON file. These lyrics just need to each be on their own line.
# Therefore, I need a way to grab the lyrics from the songs in each JSON file and insert
# them into a file artist by artist. Then, I will want to shuffle this dataset to avoid
# training bias.

# grab all filenames of scraped json lyrics data
path = "/home/alshelt/freestyle_rap_generator"
prefix = "Lyrics_"

filenames = []
for _, _, files in os.walk(path):
    for filename in files:
            if filename.startswith(prefix):
                filenames.append(filename)

# Loop through each file
# get rid of existing newlines in lyrics and replace them with periods and spaces
# write all lyrics to a string with newlines between each string
lyrics = ""
for filename in filenames:
    with open(filename) as f:
        artist_data = json.load(f)
    
    for song in artist_data["songs"]:
        lyrics += song["lyrics"].replace("\n", ". ") + "\n"

with open("lyrics_data.txt", "w") as f:
    f.write(lyrics)

