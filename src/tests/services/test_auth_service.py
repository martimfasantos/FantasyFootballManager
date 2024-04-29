# tests/test_auth_service.py

import unittest
from ..services.auth_service import AuthService

class TestAuthService(unittest.TestCase):
    def test_register_user(self):
        user = AuthService.register_user('test_user', 'test_password')
        self.assertEqual(user.username, 'test_user')
