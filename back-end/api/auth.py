from flask import Blueprint, request, jsonify
from supabase_db.supabase_client import supabase
import hashlib

auth_bp = Blueprint("auth", __name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))
    username = data.get("username")

    existing_user = supabase.table("users").select("*").eq("email", email).execute()
    if existing_user.data:
        return jsonify({"error": "Email already exists"}), 400

    res = supabase.table("users").insert({
        "email": email,
        "username": username,
        "password_hash": password
    }).execute()

    return jsonify({"message": "User created", "user": res.data[0]['id']}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = hash_password(data.get("password"))

    res = supabase.table("users").select("*").eq("email", email).eq("password_hash", password).execute()

    if res.data:
        return jsonify({"message": "Login successful", "user": res.data[0]['id']})
    else:
        return jsonify({"error": "Invalid credentials"}), 401
