import json

def load_db(path):
    with open(path, "r") as f:
        return json.load(f)

def save_db(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def add_task(title, date):
    tasks = load_db("database/tasks.json")
    tasks.append({"title": title, "date": date})
    save_db("database/tasks.json", tasks)
    return {"status": "task_created", "title": title, "date": date}

def add_incident(description, priority):
    incidents = load_db("database/incidents.json")
    incidents.append({"description": description, "priority": priority})
    save_db("database/incidents.json", incidents)
    return {"status": "incident_logged", "description": description}
