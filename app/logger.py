import logging
from logging.handlers import RotatingFileHandler
from app.config.log import LOG_SETTING
import sys
import datetime

# std out logging standar 
# author: Dodo

extra = {'port': LOG_SETTING['port'], 'now_format': datetime.datetime.now() }

logger = logging.getLogger(__name__)
syslog = logging.StreamHandler(sys.stderr)

logging.addLevelName(logging.ERROR, "error") 
logging.addLevelName(logging.WARNING, "warn")
logging.addLevelName(logging.INFO, "info")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('{ "timestamp":"%(now_format)s", "level":"%(levelname)s", "message":"%(message)s %(pathname)s:%(lineno)d","port":"%(port)s" }')
syslog.setFormatter(formatter)

logger.addHandler(syslog)

logger = logging.LoggerAdapter(logger, extra) 
