from app import app, db
from models import Flashcard

with app.app_context():
    sample_flashcards = [
        Flashcard(dish='Pasta', beverage='Wine', ingredients='Pasta, Tomato, Basil, Cheese', category='Italian'),
        Flashcard(dish='Sushi', beverage='Sake', ingredients='Rice, Fish, Seaweed', category='Japanese')
    ]
    db.session.bulk_save_objects(sample_flashcards)
    db.session.commit()