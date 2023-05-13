import os

from flask import Flask, jsonify
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# checking if url, key are set as env variables
if not url or not key:
    raise ValueError("ENV variables not set!")

# app config
api = Flask(__name__)
supabase: Client = create_client(url, key)


@api.get("/packages/<slug>")
def get_package(slug):
    # searching for the column with 'slug_name' equal to 'slug'
    response = supabase.table("packages").select("*").eq("slug_name", slug).execute()
    # returning the response as JSON
    return response.data[0]


@api.route("/")
def home():
    return "👀 Curiosity kills the 🐱 cat!"


if __name__ == "__main__":
    api.run()
