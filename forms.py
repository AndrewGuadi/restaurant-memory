from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class FlashcardForm(FlaskForm):
    dish = StringField('Dish', validators=[DataRequired()])
    beverage = StringField('Beverage', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Bar Beverages', 'Bar Beverages'), ('Appetizers', 'Appetizers'), ('Main Dishes', 'Main Dishes'), ('Desserts', 'Desserts'), ('Sides', 'Sides')], validators=[DataRequired()])
    submit = SubmitField('Submit')
