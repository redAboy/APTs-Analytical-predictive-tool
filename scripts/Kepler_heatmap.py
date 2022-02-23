# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import csv

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_MLR_Prediction_Results_Map

newcollection = db.APT_MLR_Prediction_HeatMap

collection_docs = collection.find()


docs = []

country_list = []

for doc in collection_docs:
    
    if doc["country1_code"] not in country_list:
        
        country_list.append(doc["country1_code"])
    
        dict_doc = {}
        
        dict_doc["country1_code"] = doc["country1_code"]
        dict_doc["latitude_1"] = doc["latitude_1"]
        dict_doc["longitude_1"] = doc["longitude_1"]
        
        aux_collection = collection.find()
        
        counter = 0
        
        for aux_doc in aux_collection: 
            if aux_doc["country1_code"] == doc["country1_code"]:
                counter += 1
                try:
                    dict_doc["acumulated_prediction_error"] += aux_doc["prediction_error"]
                except:
                    dict_doc["acumulated_prediction_error"] = aux_doc["prediction_error"]
                    
        dict_doc["acumulated_prediction_error"] = dict_doc["acumulated_prediction_error"] /counter
        
        docs.append(dict_doc)

newcollection.insert_many(docs)
