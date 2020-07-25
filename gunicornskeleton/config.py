# -*- coding: utf-8 -*-
import configparser
import os


# config file
config_file = os.getenv(
    "CONFIG_SETTINGS", "/usr/local/opt/gunicorn-skeleton/configs/local.ini"
)


# define config parser
config = configparser.ConfigParser(allow_no_value=True)
config.read(config_file)
