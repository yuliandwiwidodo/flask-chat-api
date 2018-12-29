from app import app
from app.library import dotenv

if __name__ == "__main__":
    app.run(
        debug=dotenv.getBoolean("DEBUG"),
        host=dotenv.getString("APP_HOST"),
        port=dotenv.getString("APP_PORT")
    )
