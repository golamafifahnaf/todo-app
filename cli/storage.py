import json

db = "tasks.json"

def load_tasks():
    try:
        with open(db, "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []
            
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_tasks(tasks):
    with open(db, "w") as file:
        json.dump(tasks, file, indent=4)