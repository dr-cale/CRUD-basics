# Endpoints, you can create multiple files if is necessary and include them into main.py
from re import match
from app.database.daos import USERS
from typing import List
from fastapi import APIRouter, Query
from sqlalchemy import text

from app.api import users
from app.api.services import UserLogic

import importlib
import uuid
daos_module = importlib.import_module("app.database.daos")

api = APIRouter()

# GET METHODS

@api.get("/health-check")
def health_check():
    message = {"HEALTH": "OK"}
    return message

@api.get("/get_user_by_firstname")
def get_user_by_firstname(firstname: str):
    try:
        return USERS.get_user_data_by_firstname(firstname)
    except Exception as e:
        return ('The following exception occurred:\n' + str(e))

@api.get("/{user_id}/get_data")
def get_user(user_id: str):
    try:
        return USERS.get_user_data(user_id)
    except Exception as e:
        return ('The following exception occurred:\n' + str(e))

# POST METHODS

@api.post("/add_user")
def add_user(user_id: str, firstname: str, lastname: str, age: int, email: str):
    try:
        uid = str(uuid.uuid1())
        user_object = {
            "user_id": uid,
            "firstname": firstname,
            "lastname": lastname,
            "age": age,
            "email": email
        }
        USERS_instance = USERS()
        return USERS_instance.add_user_data(user_object)
    except Exception as e:
        return ('The following exception occurred:\n' + str(e))

# PUT/UPDATE METHODS

@api.put('/{user_id}/update')
def update_users_age(user_id: str, age: int):
    try:
        USERS_instance = USERS()
        return USERS_instance.update_user_age(user_id, age)
    except Exception as e:
        return ('The following exception occurred:\n' + str(e))

# DELETE METHODS

@api.delete('/{user_id}/delete')
def delete_users(user_id: str):
    try:
        USERS_instance = USERS()
        return USERS_instance.delete_user(user_id)
    except Exception as e:
        return ('The following exception occurred:\n' + str(e))
