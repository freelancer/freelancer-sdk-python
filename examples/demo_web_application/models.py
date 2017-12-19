from flask import Flask
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    access_token = db.Column(db.String())
    refresh_token = db.Column(db.String())
    projects = db.relationship("Project", backref="users", uselist=False)
    def __init__(self, name, email, access_token, refresh_token):
        self.name = name
        self.email = email
        self.access_token = access_token
        self.refresh_token = refresh_token

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, project_id, user_id):
        self.project_id = project_id
        self.user_id = user_id