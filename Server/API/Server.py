from bson import json_util
from pymongo import MongoClient
from fastapi import FastAPI
from flask import Flask, jsonify
app = FastAPI()
path = r'C:/Users/JoshDev/Downloads/testset.csv'


client = MongoClient("mongodb://localhost:27017/") 
db = client["weather_db"]
collection = db["weather_data"]
#Date Lookup Endpoint




@app.get('/date-lookup/')
async def date_lookup(date: str):
    date_val = date[4:] + date[2:4] + date[:2]
    print(date_val)
    data = list(collection.find({"datetime_utc": date_val}))

    if len(data) > 0:
        return json_util.dumps(data)
    else:
        return "Not Found In Database"


#Month Lookup Endpoint

@app.get('/month-lookup/')
async def month_lookup(month: str):
    # Query MongoDB for all records where the month matches the given input
    data = list(collection.find({"datetime_utc": {"$regex": f"^{month}"}}))

    if len(data) > 0:
        return json_util.dumps(data)
    else:
        return "Not Found In Database"


#Highest Temperature per Month Endpoint (Default 0)
@app.get('/high-temp')
async def high_temp(year: str):
    months = {i: -float('inf') for i in range(1, 13)}


    data = collection.find({"date":year})


    for record in data:
        month = int(record['date'][4:6])  
        temp = record['temperature']
        if temp > months[month]:
            months[month] = temp

    return months


                    
           

@app.get('/median-temp')
async def median_temp(year: str):
    months = {i: [] for i in range(1, 13)}  


    data = collection.find({"date":year})

    for record in data:
        month = int(record['date'][4:6]) 
        temp = record['temperature']
        months[month].append(temp)

    median_temps = {}
    for month, temps in months.items():
        if temps:
            temps.sort()
            n = len(temps)
            median = temps[n // 2] if n % 2 != 0 else (temps[n // 2 - 1] + temps[n // 2]) / 2
            median_temps[month] = median
        else:
            median_temps[month] = None  

    return median_temps




#Minimum Temperature per Month Endpoint (Default 9999)

@app.get('/minimum-temp')
async def minimum_temp(year: str):
    months = {i: float('inf') for i in range(1, 13)} 

    data = collection.find({"date": year})


    for record in data:
        month = int(record['date'][4:6])  
        temp = record['temperature']
        if temp < months[month]:
            months[month] = temp

    return months
#
@app.get('/filter')
async def filter_data(temp_below: int = None):
    query = {}
    stb = ''
    for i in str(temp_below):
        stb = stb+i
    if temp_below is not None:
        query['_tempm'] = {'$lt' : stb}
    print(query)


    # Query MongoDB using the filter
    filtered_data = list(collection.find(query))
    
    if filtered_data:
        return filtered_data
    return {"message": "No data found matching the filter"}
