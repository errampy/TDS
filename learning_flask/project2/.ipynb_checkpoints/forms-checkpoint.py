import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = wtforms.StringField(validators=[DataRequired()])
    phone_number = wtforms.IntegerField(validators=[DataRequired()])
    email = wtforms.EmailField(validators=[DataRequired()])
    message = wtforms.TextAreaField(validators=[DataRequired()])
    submit = wtforms.SubmitField()
