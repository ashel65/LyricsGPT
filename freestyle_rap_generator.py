from transformers import AutoTokenizer, pipeline
from lyricsgenius import Genius

# parse artist names into array
with open("rap_artists.txt", "r", encoding="utf-8") as f:
    artist_names = [i[:-1] for i in f.readlines() if "[" not in i]

token = "7Qre4uy98X49_3FsxeXUOtV1ePsxHBZPBIE2xtyHWhHyty1ShrL6nVad7tXh-CFx"

# grab lyrics from songs from all artists in rap_artists.txt
genius = Genius(token)
for name in artist_names:
    artist = genius.search_artist(name)
    artist.save_lyrics()

generator = pipeline('')