#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Owner, Business

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://bilalhalal:password@localhost/halalworlddb",
                SECRET_KEY='YOUR_SECRET_KEY',
                DEBUG=TRUE
                )
        return app

    def setUp(self):
        db.create_all()
        sampleowner = Owner(name = 'John')
        samplebusiness = Business(name = "JohnO Ltd.", owner = sampleowner.name)
        db.session.add(sample1)
        db.session.add(samplebusiness)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

