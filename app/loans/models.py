from app import db
# Define the Loan class for the 'loan' table in the database
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loaner_id = db.Column(db.Integer, db.ForeignKey('loaner.id'), nullable=False)
    loaned_date = db.Column(db.Date, nullable=False)
    returned_date = db.Column(db.Date)  # New column for returned date

    def __init__(self, book_id, loaner_id, loaned_date, returned_date=None):
        self.book_id = book_id
        self.loaner_id = loaner_id
        self.loaned_date = loaned_date
        self.returned_date = returned_date