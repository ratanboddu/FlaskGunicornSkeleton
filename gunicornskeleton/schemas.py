# -*- coding: utf-8 -*-
from marshmallow import ValidationError, fields, schema


class BytesField(fields.Field):
    def _validate(self, value):
        if type(value) is not bytes:
            raise ValidationError("Invalid input type.")

        if value is None or value == b"":
            raise ValidationError("Invalid value")


class SchemaMixin:
    id = fields.Str()
    created_by = fields.Str()
    created_on = fields.DateTime(dump_only=True)
    last_modified_by = fields.Str()
    last_modified_on = fields.DateTime(dump_only=True)
