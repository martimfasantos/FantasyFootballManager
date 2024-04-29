# app/db.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

DB_NAME = "database.db"
db = SQLAlchemy()

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

def create_db(app: Flask, reset: bool):
    with app.app_context():
        # Create the database if it doesn't exist
        if not os.path.exists('instance/' + DB_NAME):
            db.create_all()
            print('Database created successfully!')
        elif reset:
            db.drop_all()
            db.create_all()
            print('Database reset successfully!')
        else:
            print('Database restored successfully!')

# DEBUG: Print the database structure
def print_db_structure(app: Flask):
    with app.app_context():
        with db.engine.connect() as con:
            sql = text("SELECT name FROM sqlite_master WHERE type='table';")
            rs = con.execute(sql)
            tables = rs.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table[0])  # Print the table name

def check_db(app: Flask):
     with app.app_context():
        with db.engine.connect() as con:
            sql = text("SELECT name FROM sqlite_master WHERE type='table';")
            rs = con.execute(sql)
            tables = rs.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table[0])  # Print the table name