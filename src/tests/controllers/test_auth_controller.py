# tests/test_auth_controller.py

import unittest
from flask import json
from ..app import create_app

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_register_user(self):
        response = self.client.post('/register', json={'username': 'test_user', 'password': 'test_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'User registered successfully!')
        self.assertEqual(data['username'], 'test_user')
