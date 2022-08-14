
from flask_login import UserMixin
from . import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    
class Newsletters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)