#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Owner, Business

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://bilalhalal:Maliha0919!@localhost/halalworlddb",
                SECRET_KEY="TEST_KEY",
                DEBUG=TRUE
                )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Owner(name = 'John', business = 'Doe')
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 405)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,405)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,405)

class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
                url_for('/add'),
                data = dict(name="MrMan", business="New Business")
            )
        self.assertIn(b'MrMan',response.data)

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
                url_for('update'),
                data = dict(newname="MrsLady"),
                )
        self.assertEqual(response.status_code,200)

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
                url_for('delete'),
                data = dict(newname="MrsLady")
                )
        self.assertEqual(response.status_code,200)
