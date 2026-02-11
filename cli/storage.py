import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []
            
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)