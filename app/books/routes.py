from flask import Blueprint, request, jsonify
from app import db
from .models import Book

# Create the books blueprint
books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_all_books():
    # Retrieve all books from the 'book' table
    books = Book.query.all()
    book_list = []
    for book in books:
        # Create a dictionary for each book's information
        book_info = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publication_year': book.publication_year,
            'genre': book.genre
        }
        book_list.append(book_info)

    return jsonify({'books': book_list})

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Retrieve a specific book by ID from the 'book' table
    book = Book.query.get(book_id)
    if book:
        # Create a dictionary for the book's information
        book_info = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publication_year': book.publication_year,
            'genre': book.genre
        }
        return jsonify(book_info)
    else:
        return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books', methods=['POST'])
def create_book():
    # Create a new book based on JSON data received in the request
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        publication_year=int(data['publication_year']),
        genre=data['genre']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Update an existing book's information based on JSON data received in the request
    book = Book.query.get(book_id)
    if book:
        data = request.get_json()
        book.title = data['title']
        book.author = data['author']
        book.publication_year = int(data['publication_year'])
        book.genre = data['genre']
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Delete an existing book from the 'book' table
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'message': 'Book not found'}), 404

@books_bp.route('/search-books', methods=['GET'])
def search_books():
    # Get the search query parameter from the request URL
    query = request.args.get('q')

    # Check if the query parameter is present
    if query is None:
        return jsonify({'message': 'Search query parameter "q" is missing'}), 400

    # Perform a case-insensitive search for books with titles containing the query
    books = Book.query.filter(Book.title.ilike(f'%{query}%')).all()

    # Create a list of book information
    book_list = []
    for book in books:
        book_info = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publication_year': book.publication_year,
            'genre': book.genre
        }
        book_list.append(book_info)

    return jsonify({'search_results': book_list})
