# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""


from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents_copy

query = { "group_country": "Unknown"}

x = collection.delete_many(query)

print(x.deleted_count, "documents deleted")