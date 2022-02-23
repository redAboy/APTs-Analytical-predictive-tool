# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents

results = collection.find()

collection = db.APT_Group_Incidents_CAMEO


for doc in results:      
    op_countries = doc["operation_countries"]
    
    if len(op_countries) > 50:
        print(doc["_id"])