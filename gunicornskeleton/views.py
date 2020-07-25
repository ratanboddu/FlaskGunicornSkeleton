# -*- coding: utf-8 -*-
from flasgger import swag_from
from flask import Response, g, json, jsonify, request, send_file
from flask.views import MethodView
from.exceptions import GenericException
from .log import debug, logger as log


class PingView(MethodView):
    @swag_from("swag/ping.yaml")
    @debug
    def get(self):
        try:
            return "pong"
        except Exception as ex:
            log.exception(ex)
            raise GenericException


class SampleView(MethodView):
    @swag_from("swag/post_sample.yaml")
    @debug
    def post(self):
        try:
            return "Hey ! This is POST"
        except Exception as ex:
            log.exception(ex)
            raise GenericException

    @swag_from("swag/get_sample.yaml")
    @debug
    def get(self):
        try:
            return "Hey ! This is GET"
        except Exception as ex:
            log.exception(ex)
            raise GenericException

    @swag_from("swag/put_sample.yaml")
    @debug
    def put(self):
        try:
            return "Hey ! This is PUT"
        except Exception as ex:
            log.exception(ex)
            raise GenericException

    @swag_from("swag/delete_sample.yaml")
    @debug
    def delete(self):
        try:
            return "Hey ! This is DELETE"
        except Exception as ex:
            log.exception(ex)
            raise GenericException
