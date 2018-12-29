from app.library import api_helper as Helper

class WelcomeController:
    def index(self):
        return Helper.response(200, "Welcome to Flask Chat Api")
