from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

DATA_FILE = "users.json"

# Load data from file (if exists)
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data to file
def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

# In-memory users (loaded at startup)
users = load_users()

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(str(user_id))
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    save_users(users)
    return jsonify(users[user_id]), 201

# PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_id = str(user_id)
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    save_users(users)
    return jsonify(users[user_id]), 200

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_id = str(user_id)
    if user_id in users:
        deleted = users.pop(user_id)
        save_users(users)
        return jsonify({"message": "User deleted", "user": deleted}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
