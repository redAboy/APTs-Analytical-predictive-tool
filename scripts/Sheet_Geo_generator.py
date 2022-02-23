# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import pandas as pd
import csv

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_GEO_Context_complete

collection_docs = collection.find()

df = pd.DataFrame(list(collection_docs))

df = df.drop(columns = ['_id', 'incident_id'])

df.to_csv('Sheet_Geo_complete.csv', index=False, decimal=',', sep=';')
