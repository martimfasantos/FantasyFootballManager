# tests/test_team_service.py

import unittest
from ..services.team_service import TeamService

class TestTeamService(unittest.TestCase):
    def test_create_team(self):
        team = TeamService.create_team('Fantasy Team', 1, 'Football')
        self.assertEqual(team.team_name, 'Fantasy Team')
        self.assertEqual(team.user_id, 1)
        self.assertEqual(team.sport, 'Football')
