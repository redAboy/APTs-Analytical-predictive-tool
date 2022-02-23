# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')

#Source
collection = db.APT_GEO_Context_full
results = collection.find()

fd_out = open ("cameo_country_codes.json", "r")

country_codes = json.load(fd_out)

data = collection.find()

#Destination
collection = db.APT_GEO_Context_raw_copy
collection.insert_many(data)
