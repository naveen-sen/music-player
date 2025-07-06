import syncedlyrics
import json
query=input("Enter Song Name: ")
lrc = syncedlyrics.search(query)
import re

data = lrc

if data is None:
    print("No lyrics found for the given song.")
    exit(1)

lines = data.split("\n")

json_data = []

pattern = r'\[(\d+:\d+\.\d+)\](.+)'
for line in lines:
    match = re.search(pattern, line)
    if match:
        timestamp,text = match.groups()
        json_entry = {
            "time": timestamp,
            "text": text
        }
        json_data.append(json_entry)
        
        json_string = json.dumps(json_data,indent=4)
        print(json_string)