# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents

results = collection.find()

fd_out = open ("cameo_country_codes.json", "r")

country_codes = json.load(fd_out)

collection = db.APT_Group_Incidents_CAMEO


for doc in results:
    if doc["group_country"] != "Unknown":
        collection.update_one({"_id" : doc["_id"]} , {"$set" : {"cameo_country": country_codes[doc["group_country"]]}})
        
    else:
        collection.update_one({"_id" : doc["_id"]} , {"$set" : {"cameo_country": "Unknown"}})
        
    op_countries = []
    print(doc["_id"])
    for op_country in doc["operation_countries"]:
        
        print(op_country)
        op_countries.append(country_codes[op_country])
    
    collection.update_one({"_id" : doc["_id"]} , {"$set" : {"cameo_operation_countries": op_countries}})
    