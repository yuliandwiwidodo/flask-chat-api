from app.library import api_helper as Helper
from flask import request, render_template

class ChatController:

    def index(self):
        return render_template("session.html")