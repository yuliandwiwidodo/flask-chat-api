import os
from app.config import dotenv

def getString(key):
    return str(os.getenv(key))


def getInt(key):
    return int(os.getenv(key))


def getBoolean(key):
    bool_def = {
        "True": True,
        "False": False,
        "true": True,
        "false": False,
        1: True,
        0: False
    }

    key = os.getenv(key)
    return bool_def[key]
