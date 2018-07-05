from flask import Flask, Response, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Card(db.Model):
   id = db.Column('card_id', db.Integer, primary_key = True)
   question = db.Column(db.String(100))
   topic = db.Column(db.String(100))

   def __init__(self, question, topic):
        self.question = question
        self.topic = topic

@app.route("/")
def index():
    try:
        record = random.choice(Card.query.all())
    except:
        record=None
    return render_template("index.html", card=record)

@app.route("/new", methods=["GET", "POST"])
def new_card():
    if request.method == "GET":
        return render_template("new.html")
    else:
        question = request.form["question"]
        topic = request.form["topic"]
        
        card = Card(question, topic)
        db.session.add(card)
        db.session.commit()

        return redirect("/")

# print(card)
Card.query.filter(Card.id == 1).delete()
db.session.commit()
print(Card.query.all())
app.run(debug=True, port=8000)