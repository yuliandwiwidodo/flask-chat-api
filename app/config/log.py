from app.library import dotenv
import os

LOG_SETTING = {
    'log_level': dotenv.getString('ERR_LOG_LEVEL'),
    'port': dotenv.getString('APP_PORT')
}
