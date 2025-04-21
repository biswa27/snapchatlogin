from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)

# Supabase credentials
SUPABASE_URL = "https://yvifnznvwxwcwapfgvwu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2aWZuem52d3h3Y3dhcGZndnd1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUyMzY0NzksImV4cCI6MjA2MDgxMjQ3OX0.60_RfkcsMtVruhowvNXpgCy4UhTkjGlrllti8dfZPD0"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    response = supabase.table("users").select("*").eq("username", username).single().execute()

    if response.error:
        return jsonify({"message": "User not found!"}), 404

    user = response.data
    if user["password"] == password:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Incorrect password!"}), 401

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Backend is running!"})
