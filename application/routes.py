#!/usr/bin/python3

from application import app, db
from application.models import Owner, Business
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField

class AddForm(FlaskForm):
    ownername = StringField('Business Owner Name')
    businessname = StringField('Business Name')
    submit = SubmitField('Add Business')

#class UpdateForm(FlaskForm):
   # oldname = StringField('Current Business Name')
  #  ownername = StringField("Business Owner's Name")
 #   newname = StringField('New Business Name')
#    submit = SubmitField('Save Changes')

def selectlist():
    return Business.query

class UpdateForm(FlaskForm):
    businessname = QuerySelectField('Select Business to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    newname = StringField('New Business Name')
    submit = SubmitField("Update Business")

class DeleteForm(FlaskForm):
    businessname = QuerySelectField('Select Business to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    submit = SubmitField("Delete Business")


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def view():
    fulllist = Business.query.with_entities(Business.name)
    return render_template('view.html', fulllist = fulllist) 

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = AddForm()

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
            return render_template('added.html')

    return render_template('add.html', form=form, message=error)


@app.route('/update', methods=['GET', 'POST'])
def update():
    error = ""
    form = UpdateForm()

    if request.method == 'POST':
        businessname = form.businessname.data
        newname = form.newname.data
        businessname.name = newname
        db.session.commit()
        return render_template('updated.html')

    return render_template('update.html', form=form, message=error)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    error = ""
    form = DeleteForm()

    if request.method == 'POST':
        businessname = form.businessname.data
        db.session.delete(businessname)
        db.session.commit()
        return render_template('deleted.html')
    
    return render_template('delete.html', form=form, message=error)
