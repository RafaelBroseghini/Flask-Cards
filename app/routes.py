from flask import render_template, request, redirect, jsonify, flash
from app import app, db
from app.models import Card, User
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
import random
import json

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect("/login")
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print(current_user)
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("/login")
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/login")    

@app.route("/")
@login_required
def index():
    try:
        u = User.query.get(current_user.id)
        record       = random.choice(u.posts.all())
        total_cards  = len(u.posts.all())
        # all_topics   = len(db.session.query(u.posts.topic.distinct()).all())
    except:
        record = None
        total_cards  = 0

    return render_template("index.html", card=record, total_cards=total_cards)

@app.route("/cards/new", methods=["GET", "POST"])
def new_card():
    if request.method == "GET":
        return render_template("new.html")
    else:
        u = User.query.get(current_user.id)
        question = request.form["question"]
        topic = request.form["topic"]
        print("here")
        card = Card(question, topic, author=u)
        print("here2")
        db.session.add(card)
        db.session.commit()

        return redirect("/")

@app.route("/cards")
def show_cards():
    cards = Card.query.all()
    content = {"items":[]}
    for c in cards:
        content["items"].append({"topic": c.topic, "question":c.question})
    print(content)
    return jsonify(content)

@app.route("/cards/<int:card_id>")
def get_card(card_id):
    card = Card.query.get(card_id)
    return render_template("show.html", card=card)

@app.route("/cards/<int:card_id>", methods=["POST"])
def edit(card_id):
    card = Card.query.get(card_id)
    card.question = request.form["question"]
    card.topic = request.form["topic"]
    
    db.session.commit()
    return redirect("/")

@app.route("/cards/<int:card_id>/delete", methods=["POST"])
def delete_card(card_id):
    Card.query.filter_by(id=card_id).delete()
    db.session.commit()
    return redirect("/")