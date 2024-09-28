# config.py
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "mysql://root:etalvarez03@localhost/contacts-crud"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
