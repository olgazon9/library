# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a function to create and return the Flask application instance
def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # SQLite database file

    # Create a SQLAlchemy database instance
    db = SQLAlchemy(app)

    # Import and register blueprints
    from app.main import main_bp
    from app.books import books_bp
    from app.loaners import loaners_bp
    from app.loans import loans_bp

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(loaners_bp, url_prefix='/loaners')
    app.register_blueprint(loans_bp, url_prefix='/loans')

    return app

# Remove the following line, as the app creation will be handled in run.py
# app = Flask(__name__)
