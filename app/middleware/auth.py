from functools import wraps
from app.library import api_helper as Helper

def check_auth():
    return dict(code=200)

def jwt_checking(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        checkAuth = check_auth()
        if checkAuth['code'] in [404, 1004, 1005]:
            return Helper.response(checkAuth['code'], checkAuth['msg'])

        return f(*args, **kwargs)
    return wrapper
