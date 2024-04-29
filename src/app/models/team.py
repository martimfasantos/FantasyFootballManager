# models/team.py

from ..database import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from ..utils.constants import Sports

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sport = db.Column(db.String(150), nullable=False)
    # players = db.relationship('Player', backref='team', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, team_name, user_id, sport):
        self.name = team_name
        self.user_id = user_id
        self.sport = sport
