import json
import random
from flask import render_template, request, redirect, jsonify, flash
from app import app, db
from app.models import Card, User
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

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
        record          = random.choice(u.posts.all())
        total_cards     = len(u.posts.all())
        all_topics_len  = len(set([t.topic for t in u.posts.all()]))
        all_topics      = sorted(set([t.topic for t in u.posts.all()]))
    except:
        record          = None
        total_cards     = 0
        all_topics_len  = 0
        all_topics      = 0

    return render_template("index.html", card=record, total_cards=total_cards, all_topics_len=all_topics_len, all_topics=all_topics)

@app.route("/cards/new", methods=["GET", "POST"])
def new_card():
    u = User.query.get(current_user.id)

    if request.method == "GET":
        all_topics = sorted(set([t.topic for t in u.posts.all()]))
        return render_template("new.html", all_topics=all_topics)
    else:
        category = request.form["category"]      
        topic = request.form["topic"]
        question = request.form["question"]

        if category == 'code':
            #using pygments to store code as html elements for highlighting.
            question = highlight(question, PythonLexer(), HtmlFormatter())

        card = Card(category, topic, question, author=u)
        db.session.add(card)
        db.session.commit()

        return redirect("/")

# All cards
@app.route("/cards")
def show_cards():
    u = User.query.get(current_user.id)
    cards = u.posts.all()
    # returns all cards in random order.
    # Good UX or no? No!!
    cards = sorted(cards, key=lambda card:card.topic)
    return render_template("cards.html", cards=cards)

# ---------------------------------------------------------------
'''
Can refactor this.

Make a form that given a certain request.form (e.g) it would handle the
constraints.

Like if checkbox == category or topic do first querying, else do second.
'''
# Cards by category: General vs Code
@app.route("/cards/category/<string:card_category>")
def get_card_category(card_category):
    u = User.query.get(current_user.id).posts.all()
    cards = [c for c in u if c.category == card_category]
    return render_template("cards.html", cards=cards)

# Cards by Topic.
@app.route("/cards/topic/<string:card_topic>")
def get_card_topic(card_topic):
    u = User.query.get(current_user.id).posts.all()
    cards = [c for c in u if c.topic == card_topic]
    print(cards)
    return render_template("cards.html", cards=cards)

# ---------------------------------------------------------------

# Show card's form with card info populated on form based on card id.
@app.route("/cards/<int:card_id>")
def get_card(card_id):
    u = User.query.get(current_user.id).posts.all()
    card = [c for c in u if c.id == card_id]
    return render_template("show.html", card=card[0])

# Update card.
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
