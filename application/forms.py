#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from application.models import Business

class AddForm(FlaskForm):
    ownername = StringField('Business Owner Name', validators=[DataRequired()])
    businessname = StringField('Business Name', validators=[DataRequired()])
    submit = SubmitField('Add Business')

def selectlist():
    return Business.query

class UpdateForm(FlaskForm):
    businessname = QuerySelectField('Select Business to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    newname = StringField('New Business Name', validators=[DataRequired()])
    submit = SubmitField("Update Business")

class DeleteForm(FlaskForm):
    businessname = QuerySelectField('Select Business to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    submit = SubmitField("Delete Business")

