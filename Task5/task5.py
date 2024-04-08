from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy data for example
users = [
    {'id': 1, 'name': 'Yatin'},
    {'id': 2, 'name': 'Alkye'}
]


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

# Endpoint for getting all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        return jsonify({'users': users, 'num_users': len(users)}), 200
    except Exception as e:
        abort(500, f"An error occurred: {str(e)}")

# Endpoint for getting a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = next((user for user in users if user['id'] == user_id), None)
        if user is None:
            abort(404, f"User with ID {user_id} not found")
        return jsonify(user), 200
    except Exception as e:
        abort(500, f"An error occurred: {str(e)}")

# Endpoint for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        if not request.json or 'name' not in request.json:
            abort(400, "Name is required")
        user = {'id': len(users) + 1, 'name': request.json['name']}
        users.append(user)
        return jsonify(user), 201
    except Exception as e:
        abort(500, f"An error occurred: {str(e)}")

# Endpoint for updating an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = next((user for user in users if user['id'] == user_id), None)
        if user is None:
            abort(404, f"User with ID {user_id} not found")
        if not request.json:
            abort(400, "No data provided")
        user['name'] = request.json.get('name', user['name'])
        return jsonify(user), 200
    except Exception as e:
        abort(500, f"An error occurred: {str(e)}")

# Endpoint for deleting a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = next((user for user in users if user['id'] == user_id), None)
        if user is None:
            abort(404, f"User with ID {user_id} not found")
        users.remove(user)
        return '', 204
    except Exception as e:
        abort(500, f"An error occurred: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
