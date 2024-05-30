from app import app, db
from models import Flashcard

with app.app_context():
    # Ensure the tables are created
    db.create_all()

    # Check if there are any flashcards already
    flashcards = Flashcard.query.all()
    if not flashcards:
        # Add sample flashcards if none exist
        sample_flashcards = [
            Flashcard(dish='Pasta', beverage='Wine', ingredients='Pasta, Tomato, Basil, Cheese', category='Italian'),
            Flashcard(dish='Sushi', beverage='Sake', ingredients='Rice, Fish, Seaweed', category='Japanese')
        ]
        db.session.bulk_save_objects(sample_flashcards)
        db.session.commit()
        print("Sample flashcards added to the database.")
    else:
        print("Flashcards already exist in the database.")
