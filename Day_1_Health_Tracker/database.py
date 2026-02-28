import json

FILE = "Health_tracker.json"

def data_load():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def data_save(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)