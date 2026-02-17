from pydantic import BaseModel

class Task(BaseModel):
    title: str
    date: str

class Incident(BaseModel):
    description: str
    priority: str
