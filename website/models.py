from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    credit = db.Column(db.Integer)
    posts = db.relationship('Post')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    credit = db.Column(db.Integer)
