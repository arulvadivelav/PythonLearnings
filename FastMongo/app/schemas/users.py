from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Age(BaseModel):
    age:int