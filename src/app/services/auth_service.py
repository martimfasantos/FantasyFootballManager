# services/auth_service.py

from ..models.user import User
from ..database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .errors import UserRegistrationUsernameAlreadyBeingUsedError, UserRegistrationEmailAlreadyBeingUsedError
from .errors import UserLoginWrongPasswordError, UserLoginEmailDoesNotExistError

class AuthService:
    users = []

    # Register a new user
    @classmethod
    def register_user(cls, email, username, password):
        if User.query.filter_by(email=email).first():
            raise UserRegistrationUsernameAlreadyBeingUsedError('Email is already being used!')
        elif User.query.filter_by(username=username).first():
            raise UserRegistrationEmailAlreadyBeingUsedError('Username is already being used!')
        else:
            new_user = User(email, username, generate_password_hash(password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

    
    # Login a user
    @classmethod
    def login_user(cls, email, password):
        user = User.query.filter_by(email=email).first()
        query = User.query.filter_by(email=email)
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return user
            else:
                raise UserLoginWrongPasswordError('Password is incorrect!')
        else:
            raise UserLoginEmailDoesNotExistError('Email does not exist!')
        
    # Logout a user
    @classmethod
    @login_required
    def logout_user(cls):
        logout_user()

    @classmethod
    def get_current_user(cls):
        return current_user

