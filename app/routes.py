from flask import render_template, request, redirect
from app import app
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