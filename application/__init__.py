#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://bilalhalal:Maliha0919!@localhost/halalworlddb"
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)

from application import routes
