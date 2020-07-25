# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask, Response
from flask_cors import CORS
from marshmallow import ValidationError
from werkzeug.exceptions import InternalServerError
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from .views import PingView, SampleView

from .config import config

# define flask application
application = Flask(__name__)
CORS(application)


# default handler
def simple(env, resp):
    resp(b"200 OK", [(b"Content-Type", b"text/plain")])
    return [b"Invalid Url"]


application.wsgi_app = DispatcherMiddleware(
    simple, {config.get("flask", "base_url"): application.wsgi_app}
)

# register request middleware
application.before_request_funcs = {}

# register response middleware
application.after_request_funcs = {}

# register error handlers
application.error_handler_spec = {}


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask Gunicorn Skeleton",
        "description": "REST API's",
        "version": "1.0.0",
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "backend",
            "route": "/docs/backend.json".format(config.get("flask", "base_url")),
        }
    ],
    "static_url_path": "/flasgger_static".format(config.get("flask", "base_url")),
    "swagger_ui": True,
    "specs_route": "/docs".format(config.get("flask", "base_url")),
    "basePath": f"{config.get('flask', 'base_url')}",
}

swag = Swagger(application, config=swagger_config, template=swagger_template)

# register apis
application.add_url_rule(
    "/v1/ping", view_func=PingView.as_view("ping_l"), methods=["GET"]
)
application.add_url_rule(
    "/v1/sample",
    view_func=SampleView.as_view("sample_crud"),
    methods=["GET", "DELETE", "PUT", "POST"],
)
