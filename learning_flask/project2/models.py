from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime

db = SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

