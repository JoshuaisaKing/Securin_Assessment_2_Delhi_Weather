import csv
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["weather_db"]
collection = db["weather_data"]


csv_file_path = "C:/Users/JoshDev/Downloads/testset.csv"

with open(csv_file_path, mode="r") as file:
    reader = csv.DictReader(file)
    data = []
    
    for row in reader:

        data.append(row)

    collection.insert_many(data)

print("CSV data inserted into MongoDB successfully.")


#Alter the datetime_utc column by removing time (this is for ease of access lol)

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") 
db = client["weather_db"]
collection = db["weather_data"]


update_count = 0  

count = collection.count_documents({})
print(f"Number of documents in collection: {count}")



for record in collection.find():
    datetime_utc = record.get('datetime_utc', '')
    
    if datetime_utc and '-' in datetime_utc:

        new_datetime_utc = datetime_utc.split('-')[0]


        result = collection.update_one(
            {'_id': record['_id']},  
            {'$set': {'datetime_utc': new_datetime_utc}} 
        )

        if result.modified_count > 0:
            update_count += 1  

print(f"Updated {update_count} documents in the collection.")
