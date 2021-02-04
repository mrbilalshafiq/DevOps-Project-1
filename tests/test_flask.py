#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase


from app import app
from application import db
from application.models import Owner, Business

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///", 
                SECRET_KEY='YOUR_KEY')
        return app

    def setUp(self):
        db.create_all()
        sampleowner = Owner(name = "Mr. Boss")
        samplebusiness = Business(name = "The New Ltd.", owner = sampleowner)

        db.session.add(sampleowner)
        db.session.add(samplebusiness)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_view_get(self):
        response = self.client.get(url_for('view'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
                
class TestAdd(TestBase):

    def test_add_post(self):
        self.client.post(url_for('add'), data=dict(name = "New", owner = "Boss"), follow_redirects=True)
        response = self.client.get(url_for('view'))
        self.assertIn(b'New', response.data)

class TestUpdate(TestBase):
    def test_update_post(self):
        self.client.post(url_for('update'), data=dict(oldname="The New Ltd.", newname="The New"), follow_redirects=True)
        response = self.client.get(url_for('view'))
        self.assertIn(b'The New', response.data)

class TestDelete(TestBase):
    def test_delete_post(self):
        self.client.post(url_for('delete'), data=dict(businessname="The New Ltd.", owner = "Mr. Boss"), follow_redirects=True)
        response = self.client.get(url_for('view'))
        self.assertEqual(response.status_code, 200)
