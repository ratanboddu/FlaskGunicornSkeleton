# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="flask-gunicorn-skeleton",
    version="1.0.0",
    description="Flask Gunicorn Skeleton",
    url="",
    author="Ratan Boddu",
    author_email="ratan.boddu@gmail.com",
    classifiers=["Programming Language :: Python :: 3.7"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flasgger==0.9.3",
        "flask==1.1.1",
        "flask-cors==3.0.8",
        "gunicorn==19.9.0",
        "marshmallow==2.19.5",
        "pyjwt==1.7.1",
        "requests-toolbelt==0.9.1",
        "sqlalchemy==1.3.5",
        "socketIO_client==0.7.2",
        "pylint==2.4.4",
        "Cython==0.29.15",
    ],
)
