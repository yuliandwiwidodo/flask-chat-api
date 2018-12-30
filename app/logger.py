import logging
from logging.handlers import RotatingFileHandler
from app.config.log import LOG_SETTING

logger = logging.getLogger(__name__)

handler = RotatingFileHandler(
    LOG_SETTING['location'],
    maxBytes=LOG_SETTING['max_bytes'],
    backupCount=LOG_SETTING['backup_count'])
handler.setLevel(logging._checkLevel(LOG_SETTING['log_level']))
handler.setFormatter(logging.Formatter('{ "timestamp":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s %(pathname)s:%(lineno)d"'))
logger.addHandler(handler)
