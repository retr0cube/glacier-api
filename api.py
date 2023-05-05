import os

from flask import Flask, jsonify
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

api = Flask(__name__)

@api.get("/api/packages/<slug>")
def get_package(slug):	
	response = supabase.table("packages").select("*").eq("slug_name", slug).execute()
	return response.data[0]

@api.route("/")
def home():
	return "👀 Curiosity kills the 🐱 cat!"

if __name__ == "__main__":
	api.run(debug=True)