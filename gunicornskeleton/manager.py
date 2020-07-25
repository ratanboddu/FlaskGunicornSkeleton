# -*- coding: utf-8 -*-
from uuid import uuid4


def uuid_generator():
    _uuid = uuid4()
    return str(_uuid)
