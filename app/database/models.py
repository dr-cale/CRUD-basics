# database models
import sqlalchemy
from sqlalchemy import String, Integer, MetaData

from app.database.db import engine
from app.utils.config import config_by_name

user_by_user_id = {
    "user_id": "f49905ba-03b2-46b9-b0f9-8e725c5502eb"
}

config = config_by_name['BasicConfig']

metadata = MetaData()

my_table = sqlalchemy.Table(
    "firsttable",
    metadata,
    sqlalchemy.Column("user_id", String(36), primary_key=True),
    sqlalchemy.Column("firstname", String(20), nullable=False),
    sqlalchemy.Column("lastname", String(50), nullable=False),
    sqlalchemy.Column("age", Integer(), nullable=False),
    sqlalchemy.Column("email", String(50), nullable=False)
)

metadata.create_all(engine)