from llama_cpp import Llama
from actions import execute

llm = Llama(model_path="models/mistral-7b-instruct.gguf", n_ctx=2048)

SYSTEM = """
You are an operations assistant.

Decide if the message contains an action.

Return ONLY JSON:

For task:
{"action":"CREATE_TASK","title":"...","date":"..."}

For incident:
{"action":"REPORT_INCIDENT","description":"...","priority":"low/medium/high"}

If nothing:
{"action":"NONE"}
"""

import json

def process_message(message):

    prompt = SYSTEM + "\nUser: " + message + "\nAssistant:"
    response = llm(prompt, max_tokens=200)
    text = response["choices"][0]["text"]

    try:
        data = json.loads(text)
        action = data.get("action","NONE")
        return execute(action, data)
    except:
        return {"status":"could_not_parse"}
