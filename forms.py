from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class FlashcardForm(FlaskForm):
    dish = StringField('Dish', validators=[DataRequired()])
    beverage = StringField('Beverage', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    submit = SubmitField('Submit')
