from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Ved", age=23),
    Person(id=2, name="Ved Sharma", age=24),
    Person(id=3, name="Ved S", age=22),
]


@app.get("/api")
def read_root():
    return DB
