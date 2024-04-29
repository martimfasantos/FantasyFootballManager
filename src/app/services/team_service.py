# services/team_service.py

from ..models.team import Team
from ..database import db

class TeamService:

    @classmethod
    def create_team(cls, team_name, user_id, sport):
        try:
            new_team = Team(team_name, user_id, sport)
            db.session.add(new_team)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def delete_team(cls, team_id):
        try:
            team = Team.query.get(team_id)
            db.session.delete(team)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e