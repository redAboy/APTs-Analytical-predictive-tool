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

incident_count_collection = db.APT_Total_incident_sent_by_country

incident_count_dict = {}


for doc in docs:
    first_country_cameo = doc["cameo_country"]
    if first_country_cameo != "Unknown":
        
        try:
            incident_count_dict[first_country_cameo] += 1
        except:
            incident_count_dict[first_country_cameo] = 1
            
incident_count_collection.insert_one(incident_count_dict)
        