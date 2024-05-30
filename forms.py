from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class FlashcardForm(FlaskForm):
    category = SelectField('Category', choices=[('Bar Beverages', 'Bar Beverages'), ('Appetizers', 'Appetizers'), ('Main Dishes', 'Main Dishes'), ('Desserts', 'Desserts'), ('Sides', 'Sides')], validators=[DataRequired()])
    dish = StringField('Dish')
    beverage = StringField('Beverage')
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        
        if not self.dish.data and not self.beverage.data:
            self.dish.errors.append('Either Dish or Beverage must be filled out.')
            self.beverage.errors.append('Either Dish or Beverage must be filled out.')
            return False

        return True
