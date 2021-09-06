# Utility helper functions
# from app.database.models import user_by_user_id

from app.database.models import user_by_user_id
print(user_by_user_id)
'''
user_by_user_id = {
    "rfmt": "firsttable"
}'''

def check_if_user_exists(user_id):
    if user_id in user_by_user_id.keys():
        return True
    else:
        return False