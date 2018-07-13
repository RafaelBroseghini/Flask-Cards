from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Card', backref='author', lazy='dynamic')

    def __init__(self, username, email):
       self.username = username
       self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Card(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   question = db.Column(db.String(100))
   topic = db.Column(db.String(100))
   timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
   def __init__(self, question, topic, author):
       self.question = question
       self.topic = topic
       self.author = author

@login.user_loader
def load_user(id):
    return User.query.get(int(id))