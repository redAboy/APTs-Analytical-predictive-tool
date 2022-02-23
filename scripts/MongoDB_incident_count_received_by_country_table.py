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

new_collection = db.APT_Total_incident_received_by_country_table

incidents_rece_collection = db.APT_Total_incidents_received_by_country

incidents_rece_doc = incidents_rece_collection.find_one({})

documents = []

countries = []

for doc in collection_docs:
    if doc['cameo_country'] != "Unknown":
        cont = 0
        country_names = doc['operation_countries']
        for country2_code in doc['cameo_operation_countries']:
            
            if country2_code not in countries:
                
                countries.append(country2_code)
                
                country2_lat = iso_country_codes_latlong[cameo_iso_country_codes[country2_code]]["lat"]
                country2_long = iso_country_codes_latlong[cameo_iso_country_codes[country2_code]]["long"]
                            
                number_inc_rec = incidents_rece_doc[str(country2_code)]
                
                doc_dict = {}
                
                doc_dict['country'] = country_names[cont]
                doc_dict['country_code'] = country2_code
                doc_dict['latitude'] = country2_lat
                doc_dict['longitude'] = country2_long
                doc_dict['incidents_received'] = number_inc_rec
                
                documents.append(doc_dict)
                
                
            cont += 1        
new_collection.insert_many(documents)