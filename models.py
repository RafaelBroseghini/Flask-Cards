from app import db

class Card(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   question = db.Column(db.String(100))
   topic = db.Column(db.String(100))