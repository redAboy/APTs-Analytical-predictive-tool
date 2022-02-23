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

new_collection = db.APT_Total_incidents_by_country_pairs_years_table

incidents_by_collection = db.APT_Total_incidents_by_country_pairs_years

incidents_by_doc = incidents_by_collection.find_one({})

documents = []

country_pairs = []

for doc in collection_docs:
    if doc['cameo_country'] != "Unknown":
        
            country1 = doc['group_country']
            country1_code = doc['cameo_country']
            
            year = doc['operation_year']
            
            country1_lat = iso_country_codes_latlong[cameo_iso_country_codes[country1_code]]["lat"]
            country1_long = iso_country_codes_latlong[cameo_iso_country_codes[country1_code]]["long"]
            
            cont = 0
            country2_names = doc['operation_countries']
            
            for country2_code in doc['cameo_operation_countries']:
                
                ident = year+"_"+country1_code+"_"+country2_code
                
                if ident not in country_pairs:

                    country_pairs.append(year+"_"+country1_code+"_"+country2_code)
                    
                    country2 = country2_names[cont]
                    
                    country2_lat = iso_country_codes_latlong[cameo_iso_country_codes[country2_code]]["lat"]
                    country2_long = iso_country_codes_latlong[cameo_iso_country_codes[country2_code]]["long"]
                    
                    number_inc = incidents_by_doc[ident]
                    
                    doc_dict = {}
                    
                    doc_dict['year'] = year
                    doc_dict['country1'] = country1
                    doc_dict['country1_code'] = country1_code
                    doc_dict['country1_latitude'] = country1_lat
                    doc_dict['country1_longitude'] = country1_long
                    doc_dict['country2'] = country2
                    doc_dict['country2_code'] = country2_code
                    doc_dict['country2_latitude'] = country2_lat
                    doc_dict['country2_longitude'] = country2_long
                    doc_dict['incidents'] = number_inc
                    
                    documents.append(doc_dict)
                cont += 1
                
                
new_collection.insert_many(documents)