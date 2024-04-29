# tests/test_team_controller.py

import unittest
from flask import json
from ..app import create_app

class TestTeamController(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_team(self):
        response = self.client.post('/teams', json={'team_name': 'Fantasy Team', 'user_id': 1, 'sport': 'Football'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Team created successfully!')
        self.assertTrue('team_id' in data)
