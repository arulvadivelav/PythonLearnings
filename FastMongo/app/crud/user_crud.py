from app.db.connection import db
from app.models.user_model import User, Age
from fastapi import HTTPException

def get_users():
    try:
        users_list = []
        users = db["userss"].find().sort("name",1).limit(10)
        for user in users:
            users_list.append(user)
        return users_list
    except:
        return HTTPException(status_code=500, detail="Something went wrong")

def create_user(user:User):
    try:
        data = {
            "name": user.name,
            "age": user.age,
        }
        db["userss"].insert_one(data)
        return {"message":"New user created successfully"}
    except:
        return HTTPException(status_code=500, detail="Something went wrong")
    
def update_user(name:str, age:Age):
    try:
        check_user = db["userss"].find_one({"name":name})
        if not check_user:
            return HTTPException(status_code=400, detail="User not found.")
        db["userss"].update_one({"name":name},{"$set":{"age":age}})
        return {"message":"User updated successfully"}
    except:
        return HTTPException(status_code=500, detail="Something went wrong")
    
def delete_user(name:str):
    try:
        check_user = db["userss"].find_one({"name":name})
        if not check_user:
            return HTTPException(status_code=400, detail="User not found.")
        db["userss"].delete_one({"name":name})
        return {"message":"User details deleted successfully"}
    except:
        return HTTPException(status_code=500, detail="Something went wrong")