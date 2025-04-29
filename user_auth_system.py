import hashlib
import uuid

users_db = {}

def hash_password(password):
    salt = uuid.uuid4().hex
    hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return hashed

def verify_password(hashed_password, input_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + input_password.encode()).hexdigest()

def register_user(username, password):
    if username in users_db:
        return False, "Username already exists."
    users_db[username] = hash_password(password)
    return True, "User registered successfully."

def login_user(username, password):
    if username not in users_db:
        return False, "Username not found."
    if verify_password(users_db[username], password):
        return True, "Login successful."
    else:
        return False, "Incorrect password."

def list_registered_users():
    return list(users_db.keys())
