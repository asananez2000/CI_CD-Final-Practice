import pytest
from app import app
from flask_testing import TestCase

class MyTest(TestCase):
    def create_app(self):
        return app

    def test_hello_world(self):
        response = self.client.get('/')
        self.assert200(response)  # assert the response status code is 200
        self.assertEqual(response.data.decode(), 'Hola Andreina')