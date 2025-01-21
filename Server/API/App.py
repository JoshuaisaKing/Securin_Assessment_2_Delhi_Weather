from flask import Flask, render_template, request, jsonify
import requests
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/") 
db = client["weather_database"]
collection = db["weather_data"]

@app.route('/show-dataset', methods=['GET'])
def show_dataset():
    # Fetch all records from the MongoDB collection
    data = list(collection.find())
    print(data)
    # Convert ObjectId to string for serialization
    for record in data:
        record['_id'] = str(record['_id'])

    # Return the data as a JSON response
    return jsonify(data)


@app.route("/", methods=["GET", "POST"])
def index():
    filtered_data = None
    
    if request.method == "POST":
        temp_below = request.form.get("temp_below")
        humidity_below = request.form.get("humidity_below")
        
        if temp_below and humidity_below:
            try:
                temp_below = float(temp_below)
                humidity_below = float(humidity_below)
                
                response = requests.get(
                    "http://localhost:8000/filter", 
                    params={"temp_below": temp_below, "humidity_below": humidity_below}
                )
                
                if response.status_code == 200:
                    filtered_data = response.json()
                else:
                    filtered_data = {"error": "Error fetching data from the backend."}
            except ValueError:
                filtered_data = {"error": "Invalid input. Please enter numeric values."}

    return render_template("index.html", filtered_data=filtered_data)

if __name__ == "__main__":
    app.run(debug=True)
