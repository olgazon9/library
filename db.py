from app import app, db
from app.books.models import Book
from app.loaners.models import Loaner
from app.loans.models import Loan

# Create the database tables
with app.app_context():
    db.create_all()
