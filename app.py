from flask import Flask, render_template, request, redirect, url_for
from models import db, Flashcard
from forms import FlashcardForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def index():
    flashcards = Flashcard.query.all()
    return render_template('index.html', flashcards=flashcards)

@app.route('/add', methods=['GET', 'POST'])
def add_card():
    form = FlashcardForm()
    if form.validate_on_submit():
        flashcard = Flashcard(dish=form.dish.data, beverage=form.beverage.data, ingredients=form.ingredients.data)
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
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_card.html', form=form)

@app.route('/delete/<int:id>')
def delete_card(id):
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/test')
def test():
    flashcards = Flashcard.query.all()
    return render_template('test.html', flashcards=flashcards)

if __name__ == '__main__':
    app.run(debug=True)
