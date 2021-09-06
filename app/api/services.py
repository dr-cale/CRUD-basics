# Business logic
import os
import json
import importlib
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from app.utils.utils import check_if_user_exists

users_module = importlib.import_module("app.database.daos")

'''user_mapper = {
    "rfmt": "RFMT"
}'''

class UserLogic:

    @staticmethod
    def get_user_logic(user_id, query_param):
        """
        This function is packing users data in format that we need.
        :param user_id: string, also name of class in our db directory(daos.py)
        :param query_param: dictionary, contains name of parameter and value that we use for filtering(firstname, lastname, age, email)
        :return: Dictionary/List[Dictionary] in format of response users
        """
        '''# Check if we have given user in our database
        if not check_if_user_exists(user_id):
            raise HTTPException(status_code=400, detail=f"User {user_id} does not exist!")

        user = getattr(users_module, user_mapper[user_id])

        # Check if value of parameter exists in database. If not return list of most similar values.
        is_valid_param, param = app.database.daos.check_if_param_exists(
            user_id=user_id,
            query_param=query_param,
            date_from=None,
            date_to=None
        )
        if not is_valid_param:
            raise HTTPException(status_code=400,
                                detail=f"There is no {list(query_param.keys())[0]}: {list(query_param.values())[0]}, try some of these: {param}")

        user_data = user.get_users(
            user_id=user_id,
            query_param=query_param,
        )
        if user_data == {}:
            return JSONResponse(status_code=204, content={
                "message": "Query returned empty results !"
            })
        return {
            "user_id": user_id,
            list(query_param.keys())[0]: list(query_param.values())[0],
            "user_data": user_data
        }'''