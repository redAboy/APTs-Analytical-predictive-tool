# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents_CAMEO
docs = collection.find()

incident_count_collection = db.APT_Total_incidents_sent_by_years

incident_count_dict = {}


for doc in docs:
    if doc["cameo_country"] != "Unknown":
        
        try:
            year = int(doc["operation_year"])
        
            key = doc["operation_year"]+"_"+doc["cameo_country"]
            
            try:
                incident_count_dict[key] += 1
            except:
                incident_count_dict[key] = 1
       
        except:
            print(doc["_id"])

incident_count_collection.insert_one(incident_count_dict)
        
