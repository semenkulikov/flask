from logging.handlers import RotatingFileHandler
import logging

log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(message)s')
my_handler = RotatingFileHandler("flask.log", mode='a', maxBytes=5 * 1024 * 1024,
                                 backupCount=1, encoding="utf8", delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.INFO)
