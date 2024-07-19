from fastapi import APIRouter
from typing import List
from app.schemas.users import User, Age
from app.crud.user_crud import create_user, delete_user, get_users, update_user

router = APIRouter()

@router.get("/users", response_model=List[User])
def get_users_list():
    return get_users()

@router.post("/users")
def create_new_user(user:User):
    return create_user(user=user)

@router.put("/users/{name}")
def update_user_details(name:str, age:Age):
    return update_user(name, age)

@router.delete("/users/{name}")
def delete_user_details(name:str):
    return delete_user(name)
