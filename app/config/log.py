from app.library import dotenv
import os

LOG_SETTING = {
    'log_level': dotenv.getString('ERR_LOG_LEVEL'),
    'port': dotenv.getString('APP_PORT'),
    'max_bytes': dotenv.getInt('ERR_LOG_MAXBYTES'),
    'backup_count': dotenv.getInt('ERR_LOG_BACKUP_COUNT'),
    'location': dotenv.getString('ERR_LOG_LOCATION')
}

