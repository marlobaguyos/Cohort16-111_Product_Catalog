#!/user/bin/env python3
#-*- coding: utf8 -*-
"""App init file"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app import routes