# utils/password_utils.py

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, stored_password):
    return hashlib.sha256(input_password.encode()).hexdigest() == stored_password

