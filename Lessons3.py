from pathlib import Path
import json 

user_name = input("What is your name? ")

# stores user's name in json file
path = Path("/workspaces/CMP2_Unit-3/Lesson 3/username.json")
contents = json.dumps(user_name) # converts to json format
path.write_text(contents) # writes to username.json

### Retrieves user's name from json file ###
contents = path.read_text() # get text from file in path
user_name_2 = json.loads(contents) # convert to Python dictionary
print(f"Welcome back {user_name_2}!")
