# -*- coding: utf-8 -*-
import logging
import sys
from logging.handlers import RotatingFileHandler

from flask import g, request

from .config import config
from .manager import uuid_generator


# define log formatter

log_format = (
    "%(asctime)s - [%(levelname)s] - %(request_id)s - %(message)s"
)
formatter = logging.Formatter(log_format)


# define rotating file handler
file_name = config.get("log", "file_name")
file_size = config.get("log", "file_size")
backup_count = config.get("log", "backup_count")
file_handler = RotatingFileHandler(
    file_name, maxBytes=int(file_size), backupCount=int(backup_count)
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


# define stream handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)


# define logger
logger = logging.getLogger("gunicorn-skeleton")
logger.setLevel(logging.DEBUG)

# add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
extra = {"request_id": None}
logger = logging.LoggerAdapter(logger, extra)


def debug(fn):
    def wrapper(*args, **kwargs):
        args_specs = locals()
        request_id = uuid_generator()
        result = None
        if "fn" in args_specs:
            del args_specs["fn"]
        if request:
            args_specs["url"] = request.url
            if not request.files:
                args_specs["json"] = (
                    request.get_json(force=True, silent=True) or request.data
                )
        extra = {"request_id": request_id}
        logger = logging.getLogger("gunicorn-skeleton")
        logger = logging.LoggerAdapter(logger, extra)
        logger.info("Entering {0} - parameters {1}".format(fn.__qualname__, args_specs))
        try:
            result = fn(*args, **kwargs)
        except Exception as e:
            logger.exception(
                "Exception in {0} - parameters {1}".format(fn.__qualname__, args_specs)
            )
            raise e
        finally:
            logger.info(
                "Finished {0} - parameters {1}".format(fn.__qualname__, args_specs)
            )
        return result

    return wrapper
