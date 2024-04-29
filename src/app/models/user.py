# models/user.py
from ..database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    teams = db.relationship('Team', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

