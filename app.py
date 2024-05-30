from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Flashcard
from forms import FlashcardForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    flashcards = Flashcard.query.all()
    return render_template('index.html', flashcards=flashcards)

@app.route('/add', methods=['GET', 'POST'])
def add_card():
    form = FlashcardForm()
    if form.validate_on_submit():
        flashcard = Flashcard(dish=form.dish.data, beverage=form.beverage.data, ingredients=form.ingredients.data, category=form.category.data)
        db.session.add(flashcard)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_card.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_card(id):
    flashcard = Flashcard.query.get_or_404(id)
    form = FlashcardForm(obj=flashcard)
    if form.validate_on_submit():
        flashcard.dish = form.dish.data
        flashcard.beverage = form.beverage.data
        flashcard.ingredients = form.ingredients.data
        flashcard.category = form.category.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_card.html', form=form)

@app.route('/delete/<int:id>')
def delete_card(id):
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        category = request.form.get('category')
        flashcard = Flashcard.query.filter_by(category=category).first()
        all_ingredients = [ingredient.strip() for ingredient in flashcard.ingredients.split(',')]
        return render_template('test.html', flashcard=flashcard, all_ingredients=all_ingredients)
    categories = Flashcard.query.with_entities(Flashcard.category).distinct()
    return render_template('select_category.html', categories=categories)

@app.route('/grade', methods=['POST'])
def grade():
    selected_ingredients = request.form.get('selected_ingredients')
    if not selected_ingredients:
        selected_ingredients = []
    else:
        selected_ingredients = selected_ingredients.split(',')

    flashcard_id = request.form.get('flashcard_id')
    flashcard = Flashcard.query.get(flashcard_id)
    correct_ingredients = [ingredient.strip() for ingredient in flashcard.ingredients.split(',')]

    correct = set(selected_ingredients) == set(correct_ingredients)
    return render_template('grade.html', correct=correct, selected_ingredients=selected_ingredients, correct_ingredients=correct_ingredients)

if __name__ == '__main__':
    app.run(debug=True)
