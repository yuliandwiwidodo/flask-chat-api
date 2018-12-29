from app import app
from app.controller.welcome_controller import WelcomeController
from app.library import api_helper as Helper
from app.middleware import auth
from flask_cors import CORS
from app.library import dotenv
from werkzeug.routing import PathConverter
import blinker as _

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Converter Url
class EverythingConverter(PathConverter):
    regex = '.*?'

app.url_map.converters['everything'] = EverythingConverter
# END converter

# Router Error #
@app.errorhandler(400)
def bad_request(error):
    return Helper.response(400, "The browser (or proxy) sent a request that this server could not understand."), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return Helper.response(405, "The method is not allowed for the requested URL."), 405

@app.errorhandler(404)
def page_not_found(error):
    return Helper.response(404, "Halaman yang Anda minta tidak tersedia."), 400

@app.errorhandler(403)
def forbidden_error(error):
    return Helper.response(403, "Anda tidak memiliki akses. Silahkan hubungi team developer."), 403

@app.errorhandler(410)
def unauthorized_eror(error):
    return Helper.response(410, "Anda tidak memiliki akses."), 410

@app.errorhandler(500)
def internal_server_error(error):
    return Helper.response(500, "Terjadi masalah pada server."), 500
# End Router Error #

# Router Basic #
@app.route("/", methods=["GET"])
def get_hello():
    return WelcomeController().index()

