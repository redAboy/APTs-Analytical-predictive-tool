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

new_collection = db.APT_Total_incident_by_group

documents = []

groups = []

total_incidents = 0

for doc in collection_docs:
    if doc['cameo_country'] != "Unknown":
        if doc['group_name'] not in groups:
        
            group = doc['group_name']
            
            groups.append(group)
            
            country = doc['group_country']
            
            country_code = doc['cameo_country']
            
            country1_lat = iso_country_codes_latlong[cameo_iso_country_codes[country_code]]["lat"]
            country1_long = iso_country_codes_latlong[cameo_iso_country_codes[country_code]]["long"]
                
            incidents = 0
            years = []
            
            for doc_counter in collection.find({'group_name': group}):
                incidents += 1
                years.append(doc_counter['operation_year'])
                     
            total_incidents += incidents
            
            doc_dict = {}
            
            doc_dict['group_name'] = group
            doc_dict['country'] = country
            doc_dict['country_code'] = country_code
            doc_dict['latitude'] = country1_lat
            doc_dict['longitude'] = country1_long
            doc_dict['incidents_sent'] = incidents
            doc_dict['year_list'] = years
            
            documents.append(doc_dict)
                    
new_collection.insert_many(documents)

print(total_incidents)