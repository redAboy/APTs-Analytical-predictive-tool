# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:13:42 2021

@author: QWERTY
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_GEO_Context_complete
docs_complete = collection.find()

new_collection = db.APT_GEO_Context_2021_missing


for doc in docs_complete:
    if int(doc['incident_year']) < 2021:
        new_collection.insert_one(doc)
        