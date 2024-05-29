from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(100), nullable=False)
    beverage = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
