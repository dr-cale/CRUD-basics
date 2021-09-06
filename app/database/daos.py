# Database access object
# Here we work with db object but business logic should be in services.py

from starlette.responses import JSONResponse
from app.api.users import SpecificUser
import difflib
from sqlalchemy import text

from app.database.db import Session, engine
from app.database import models
from app.database.models import user_by_user_id, my_table

db = Session()
load_instance = True
engine = engine

class USERS:

    @staticmethod
    def get_user_data(user: SpecificUser):
        try:
            query = text(
                    """
                    SELECT * from firsttable where user_id = :id;
                    """).params(id = user)
            results = db.execute(query).fetchall()
            return results
        except Exception as e:
            str(e)

    @staticmethod
    def get_user_data_by_firstname(user: SpecificUser):
        try:
            query = text(
                """
                SELECT * from firsttable where firstname = :firstname;
                """).params(firstname = user)
            results = db.execute(query).fetchall()
            return results
        except Exception as e:
            str(e)
    
    @staticmethod
    def add_user_data(user: SpecificUser):
        try:
            print(my_table)
            query = my_table.insert().values(
                user_id = user["user_id"],
                firstname = user["firstname"],
                lastname = user["lastname"],
                age = user["age"],
                email = user["email"]
            )
            print(user)
            engine.execute(query)
            return "Success"
        except Exception as e:
            return str(e)
    
    @staticmethod
    def update_user_age(user_id, age):
        check_if_user_exists = f"select user_id from firsttable where user_id = '{user_id}'"

        if engine.execute(check_if_user_exists).first() is not None:
            query = f"update firsttable set age = {age} where user_id = '{user_id}'"
            engine.execute(query)

            return JSONResponse(
                status_code=200,
                content={
                    'Result': 'User successfully updated.'
                }
            )
        else:
            return ('The user ID does not exist.')

    @staticmethod
    def delete_user(user: SpecificUser):
        check_if_user_exists = f"select user_id from firsttable where user_id = '{user}'"

        if engine.execute(check_if_user_exists).first() is not None:
            query = f"delete from firsttable where user_id = '{user}'"
            engine.execute(query)

            return JSONResponse(
                status_code=200,
                content={
                    'Result': 'User successfully deleted.'
                }
            )
        else:
            return JSONResponse(
                status_code=404,
                content={
                    'Result': 'The user ID does not exist.'
                }
            )
