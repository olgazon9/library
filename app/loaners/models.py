from app import db
# Define the Loaner class for the 'loaner' table in the database
class Loaner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact