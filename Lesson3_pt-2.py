from pathlib import path
import json

song_info = {}
song_info["Artist"] = "David Bowie"
song_info["Title"] = "Heroes"
song_info["Release Year"] = 1977
song_info["Modern"] = False

print(song_info)

path = Path("CMP2_Unit-3/song_info.json")
contents = json.dumps(song_info) # convert Python dictionary to Json format
path.write_text(contents) # write to Json file

print(contents)


# python has '' and json has "" and False is false in json file while its False in ptyhon

# Read content from json file
contents = path.read_text()
song_info = json.loads(contents) # converts json to python dictionary
print(song_info)
print(type(song_info["Modern"]))

# homework is 10-11 through 10-14 pg 206
