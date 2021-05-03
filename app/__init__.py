#!/user/bin/env python3
#-*- coding: utf8 -*-
"""App init file"""

from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dp = SQLAlchemy(app)

from app import routes