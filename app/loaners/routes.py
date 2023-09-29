from flask import Blueprint, request, jsonify
from app import db
from .models import Loaner

# Create the loaners blueprint
loaners_bp = Blueprint('loaners', __name__)

@loaners_bp.route('/loaners', methods=['GET'])
def get_all_loaners():
    # Retrieve all loaners from the 'loaner' table
    loaners = Loaner.query.all()
    loaner_list = []
    for loaner in loaners:
        # Create a dictionary for each loaner's information
        loaner_info = {
            'id': loaner.id,
            'name': loaner.name,
            'contact': loaner.contact
        }
        loaner_list.append(loaner_info)

    return jsonify({'loaners': loaner_list})

@loaners_bp.route('/loaners/<int:loaner_id>', methods=['GET'])
def get_loaner(loaner_id):
    # Retrieve a specific loaner by ID from the 'loaner' table
    loaner = Loaner.query.get(loaner_id)
    if loaner:
        # Create a dictionary for the loaner's information
        loaner_info = {
            'id': loaner.id,
            'name': loaner.name,
            'contact': loaner.contact
        }
        return jsonify(loaner_info)
    else:
        return jsonify({'message': 'Loaner not found'}), 404

@loaners_bp.route('/loaners', methods=['POST'])
def create_loaner():
    # Create a new loaner based on JSON data received in the request
    data = request.get_json()
    new_loaner = Loaner(
        name=data['name'],
        contact=data['contact']
    )
    db.session.add(new_loaner)
    db.session.commit()
    return jsonify({'message': 'Loaner created successfully'}), 201

@loaners_bp.route('/loaners/<int:loaner_id>', methods=['PUT'])
def update_loaner(loaner_id):
    # Update an existing loaner's information based on JSON data received in the request
    loaner = Loaner.query.get(loaner_id)
    if loaner:
        data = request.get_json()
        loaner.name = data['name']
        loaner.contact = data['contact']
        db.session.commit()
        return jsonify({'message': 'Loaner updated successfully'})
    else:
        return jsonify({'message': 'Loaner not found'}), 404

@loaners_bp.route('/loaners/<int:loaner_id>', methods=['DELETE'])
def delete_loaner(loaner_id):
    # Delete an existing loaner from the 'loaner' table
    loaner = Loaner.query.get(loaner_id)
    if loaner:
        db.session.delete(loaner)
        db.session.commit()
        return jsonify({'message': 'Loaner deleted successfully'})
    else:
        return jsonify({'message': 'Loaner not found'}), 404

@loaners_bp.route('/search-loaners', methods=['GET'])
def search_loaners_by_name():
    # Get the search query parameter 'name' from the request URL
    query_name = request.args.get('name')

    # Check if the 'name' query parameter is present
    if query_name is None:
        return jsonify({'message': 'Search query parameter "name" is missing'}), 400

    # Perform a case-insensitive search for loaners with names containing the query
    loaners = Loaner.query.filter(Loaner.name.ilike(f'%{query_name}%')).all()

    # Create a list of loaner information
    loaner_list = []
    for loaner in loaners:
        loaner_info = {
            'id': loaner.id,
            'name': loaner.name,
            'contact': loaner.contact
        }
        loaner_list.append(loaner_info)

    return jsonify({'search_results': loaner_list})
