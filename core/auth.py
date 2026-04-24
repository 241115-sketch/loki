import json
import hashlib
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = BASE_DIR / "config" / "users.json"

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    os.makedirs(USERS_FILE.parent, exist_ok=True)
    
    users = {}
    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                users = json.load(f)
        except Exception:
            users = {}

    if username in users:
        return False, "User already exists."

    users[username] = {
        "password": _hash_password(password)
    }

    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)
    
    return True, "Registration successful."

def login_user(username, password):
    if not USERS_FILE.exists():
        return False, "No users registered."

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        return False, "Database error."

    if username not in users:
        return False, "User not found."

    if users[username]["password"] == _hash_password(password):
        return True, "Login successful."
    else:
        return False, "Incorrect password."
