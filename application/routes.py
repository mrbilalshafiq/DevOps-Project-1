#!/usr/bin/python3

from application import app, db
from application.models import Owner, Business
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class BasicForm(FlaskForm):
    ownername = StringField('Business Owner Name')
    businessname = StringField('Business Name')
    submit = SubmitField('Add Businesse')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        ownername = form.ownername.data
        businessname = form.businessname.data

        owner = Owner(name = ownername)
        db.session.add(owner)
        db.session.commit()
        business = Business(name = businessname, owner = Owner.query.filter_by(name=ownername).first())
        db.session.add(business)
        db.session.commit()

        if len(ownername) == 0 or len(businessname) == 0:
            error = "Please supply both your name and the business name"
        else:
            return 'You have now been added'

    return render_template('add.html', form=form, message=error)

#@app.route('/add')
#def add():
#    new_game = Games(name="New Game")
#    db.session.add(new_game)
#    db.session.commit()
#    return "Added new game to database"

#@app.route('/read')
#def read():
#    all_games = Games.query.all()
#    games_string = ""
#    for game in all_games:
#        games_string += "<br>"+ game.name
#    return games_string

#@app.route('/update/<name>')
#def update(name):
#    first_game = Games.query.first()
#    first_game.name = name
#    db.session.commit()
#    return first_game.name

#@app.route('/delete')
#def delete():
#    delete_game = Games.query.first()
#    db.session.delete(delete_game)
#    db.session.commit()
#    return "Deleted gane"
