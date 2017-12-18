from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    access_token = db.Column(db.String())
    refresh_token = db.Column(db.String())

    def __init__(self, name, email, access_token, refresh_token):
        self.name = name
        self.email = email
        self.access_token = access_token
        self.refresh_token = refresh_token