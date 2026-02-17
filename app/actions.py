from memory import add_task, add_incident

def execute(action, data):

    if action == "CREATE_TASK":
        return add_task(data["title"], data["date"])

    if action == "REPORT_INCIDENT":
        return add_incident(data["description"], data["priority"])

    return {"status": "no_action"}
