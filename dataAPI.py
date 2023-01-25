import pymongo
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/ip", methods=["GET", "POST"])
def get_or_create_ip():
    # place the above script here
    return jsonify({"message": "success"})
# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://LukeNewman:shipping4U@cluster0.hjxmhf7.mongodb.net/")

# Get the "user_data" database
db = client["user_data"]

# Get the "ips" collection
ips_collection = db["ips"]

# Get the IP address from the incoming data
ip = "153.2.2"

# Check if the IP address already exists in the collection
existing_note = ips_collection.find_one({"ip": ip})

if existing_note:
    # If the IP address already exists, update the "guesses" field
    ips_collection.update_one({"ip": ip}, {"$inc": {"guesses": 1}})
else:
    # If the IP address does not exist, insert a new document with the IP address and initial "guesses" value
    ips_collection.insert_one({"ip": ip, "guesses": 1})

# Find all documents in the collection
for doc in ips_collection.find():
    print(doc)
