from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, Flashcard
from forms import FlashcardForm
from flask_migrate import Migrate
import random

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

@app.route('/select_category', methods=['GET', 'POST'])
def select_category():
    if request.method == 'POST':
        category = request.form.get('category')
        flashcards = Flashcard.query.filter_by(category=category).all()
        print(f"Selected Category: {category}, Flashcards: {flashcards}")  # Debugging statement
        session['flashcards'] = [flashcard.id for flashcard in flashcards]
        session['current_flashcard_index'] = 0
        session['results'] = []
        return redirect(url_for('test'))
    categories = Flashcard.query.with_entities(Flashcard.category).distinct()
    return render_template('select_category.html', categories=categories)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        flashcard_id = request.form['flashcard_id']
        selected_ingredients = request.form['selected_ingredients'].split(',')
        flashcard = Flashcard.query.get(flashcard_id)
        correct_ingredients = [ingredient.strip() for ingredient in flashcard.ingredients.split(',')]
        is_correct = set(selected_ingredients) == set(correct_ingredients)

        result = {
            'flashcard_id': flashcard_id,
            'dish': flashcard.dish,
            'beverage': flashcard.beverage,
            'selected_ingredients': selected_ingredients,
            'correct_ingredients': correct_ingredients,
            'is_correct': is_correct
        }
        results = session.get('results', [])
        results.append(result)
        session['results'] = results

        current_index = session['current_flashcard_index']
        session['current_flashcard_index'] += 1

        if current_index >= len(session['flashcards']):
            return render_template('results.html', results=results)

        flashcard_id = session['flashcards'][current_index]
        flashcard = Flashcard.query.get(flashcard_id)
        all_ingredients = {ingredient.strip() for fc in Flashcard.query.all() for ingredient in fc.ingredients.split(',')}
        categorized_ingredients = categorize_ingredients(all_ingredients, correct_ingredients)
        return render_template('test.html', flashcard=flashcard, **categorized_ingredients, result=result)

    current_index = session.get('current_flashcard_index', 0)
    flashcards = session.get('flashcards', [])
    if current_index >= len(flashcards):
        results = session.pop('results', [])
        return render_template('results.html', results=results)

    flashcard_id = flashcards[current_index]
    flashcard = Flashcard.query.get(flashcard_id)
    all_ingredients = {ingredient.strip() for fc in Flashcard.query.all() for ingredient in fc.ingredients.split(',')}
    correct_ingredients = [ingredient.strip() for ingredient in flashcard.ingredients.split(',')]
    categorized_ingredients = categorize_ingredients(all_ingredients, correct_ingredients)
    return render_template('test.html', flashcard=flashcard, **categorized_ingredients)

def categorize_ingredients(ingredients, correct_ingredients, limit=5):
    def categorize(ingredient):
        if 'water' in ingredient or 'juice' in ingredient or 'syrup' in ingredient:
            return 'liquids'
        elif 'powder' in ingredient or 'sugar' in ingredient:
            return 'solids'
        else:
            return 'garnishes'

    categorized = {'liquids': [], 'solids': [], 'garnishes': []}
    correct_categorized = {'liquids': [], 'solids': [], 'garnishes': []}

    for ingredient in ingredients:
        category = categorize(ingredient)
        categorized[category].append(ingredient)
        if ingredient in correct_ingredients:
            correct_categorized[category].append(ingredient)

    def get_limited_category(category):
        correct_items = correct_categorized[category]
        optional_items = [ing for ing in categorized[category] if ing not in correct_items]
        if len(correct_items) >= limit:
            return correct_items[:limit]
        else:
            return correct_items + random.sample(optional_items, min(limit - len(correct_items), len(optional_items)))

    return {
        'liquids': get_limited_category('liquids'),
        'solids': get_limited_category('solids'),
        'garnishes': get_limited_category('garnishes')
    }
if __name__ == '__main__':
    app.run(debug=True)
