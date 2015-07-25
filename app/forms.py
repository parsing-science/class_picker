from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class StudentsListForm(Form):
    studentlist = StringField('students-list', validators=[DataRequired()])