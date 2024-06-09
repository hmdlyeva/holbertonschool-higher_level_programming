#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

# Basic Authentication
auth = HTTPBasicAuth()

# JWT Authentication
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
jwt = JWTManager(app)

# User data (in-memory for demonstration)
users = {
    "user1": {"username": "user1", "password": "pbkdf2:sha256:150000$s0gPdS7Y$1616ff2189d148a30d2f21877f8d384f6db0d27c0ee6ff1d27c6c08602a40e25", "role": "user"},
    "admin1": {"username": "admin1", "password": "pbkdf2:sha256:150000$s0gPdS7Y$1616ff2189d148a30d2f21877f8d384f6db0d27c0ee6ff1d27c6c08602a40e25", "role": "admin"}
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username]['password'] == password:
        return username

# JWT Authentication - Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username]['password'] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Protected Route - Basic Authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Protected Route - JWT Authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Protected Route - Role-based Access Control
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Unauthorized access"}), 403

if __name__ == '__main__':
    app.run(debug=True)
