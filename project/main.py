
import json
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from .models import Newsletters
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    letters = Newsletters.query.all()
    return render_template('index.html', newsletters=letters)
    
@main.route('/detail/<letter_id>')
def detail(letter_id):
    letter = Newsletters.query.filter_by(id=letter_id).first()
    return render_template('detail.html', letter=letter)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)

@main.route('/addnews')
@login_required
def addnews():
    return render_template('addnews.html')


@main.route('/addnews', methods=['POST'])
@login_required
def addnews_post():
    # get last news id for new record. 
    newsid = Newsletters.query.order_by(Newsletters.id.desc()).first()
    if newsid == None:
        id = 1
    else:
        id = int(newsid.id) + 1
    header = request.form.get('header')
    body = request.form.get('body')
    topic = request.form.get('topic')
    author = request.form.get('author')

    # create news with the form data.
    add_news = Newsletters(id=id, header=header, body=body, topic=topic, author=author)

    # add the news to the database.
    db.session.add(add_news)
    db.session.commit()

    return redirect(url_for('main.addnews'))

# API for get the list of newsletter
@main.route('/list', methods=['POST'])
def list():
    letters = Newsletters.query.all()
    all_letters = []
    for letter in letters:
        new_letter = {
            "id": letter.id,
            "header": letter.header,
            "topic": letter.topic
        }
        all_letters.append(new_letter)
    return json.dumps(all_letters), 200

# API for get the detail of newsletter
@main.route('/detail/<letter_id>', methods=['POST'])
def detail_post(letter_id):
    letter = Newsletters.query.filter_by(id=letter_id).first()
    new_letter=[{"id":letter.id,"header":letter.header,"body":letter.body,"topic":letter.topic,"author":letter.author}]
    return json.dumps(new_letter), 200