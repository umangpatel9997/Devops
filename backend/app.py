from flask import Flask, request,jsonify
import json
from datetime import datetime
from dotenv import load_dotenv
import os  
import urllib.parse
import pymongo
#from pymongo.server_api import ServerApi

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')


# Escape the password for the connection string
escaped_USERNAME = urllib.parse.quote_plus(MONGO_USERNAME)
escaped_PASSWORD = urllib.parse.quote_plus(MONGO_PASSWORD)

url1 = MONGO_URI.replace("<username>",escaped_USERNAME)
# print(url1) 
url = url1.replace("<password>",escaped_PASSWORD)
# print(url)
#uri = f"mongodb+srv://sa:{escaped_password}@testdb.didbxgb.mongodb.net/?retryWrites=true&w=majority&appName=TestDB"

# Create a new client and connect to the server
client = pymongo.MongoClient(url)

MongoDB = client.TestDB

collection = MongoDB['flask-tutorial']
Itemcollection = MongoDB['flask-tutorial-ItemCollection']

app = Flask(__name__)
  
@app.route("/submit",methods=['POST'])
def submit() :
    form_data =dict(request.json)
    
    collection.insert_one(form_data)
    res = {
       'message' : "Data Submitted Successfully"
    }
    return res

@app.route("/submittodoitem",methods=['POST'])
def submittodoitem() :
    form_data =dict(request.json)
    
    Itemcollection.insert_one(form_data)
    res = {
       'message' : "Data Submitted Successfully"
    }
    return res



@app.route("/view")
def view():
    data = collection.find()
    data = list(data)
    for item in data :
        
        del item['_id']
    data = {
        'data':data
    }
    return data

@app.route("/fileview")
def fileview():
    try:
        with open('example_1.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data.json"}), 500
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True )