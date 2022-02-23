# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import json

with open ("cameo_to_iso3166.json", "r") as fd_out:
    cameo_iso_country_codes = json.load(fd_out)
    
#Iso country lat and longs loading
with open ("countrycode-latlong.json", "r") as fd_out:
    iso_country_codes_latlong = json.load(fd_out)

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents_CAMEO

collection_docs = collection.find()

new_collection = db.APT_Total_incidents_sent_by_years_table

incidents_by_collection = db.APT_Total_incidents_sent_by_years

incidents_by_doc = incidents_by_collection.find_one()

documents = []

sent_pairs = []

for doc in collection_docs:
    if doc['cameo_country'] != "Unknown":

        country1 = doc['group_country']
        country1_code = doc['cameo_country']
            
        year = doc['operation_year']
        
        key = year+"_"+country1_code
        
        if key not in sent_pairs:
            sent_pairs.append(key)
            
            country1_lat = iso_country_codes_latlong[cameo_iso_country_codes[country1_code]]["lat"]
            country1_long = iso_country_codes_latlong[cameo_iso_country_codes[country1_code]]["long"]
                 
            number_inc = incidents_by_doc[key]
            
            doc_dict = {}
            
            doc_dict['year'] = year
            doc_dict['country'] = country1
            doc_dict['country_code'] = country1_code
            doc_dict['latitude'] = country1_lat
            doc_dict['longitude'] = country1_long
            doc_dict['incidents'] = number_inc
            
            documents.append(doc_dict)
                
                
                
new_collection.insert_many(documents)