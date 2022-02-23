# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient
import json
import csv

with open ("cameo_to_iso3166.json", "r") as fd_out:
    cameo_iso_country_codes = json.load(fd_out)
    
#Iso country lat and longs loading
with open ("countrycode-latlong.json", "r") as fd_out:
    iso_country_codes_latlong = json.load(fd_out)

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents_CAMEO

collection_docs = collection.find()

countries = []

matrix = [ [ 0 for i in range(197) ] for j in range(197) ]

for doc in collection_docs:
    if doc['cameo_country'] != "Unknown":
        if doc['cameo_country'] not in countries:
            countries.append(doc['cameo_country'])
            
        x_index = countries.index(doc['cameo_country'])
            
        for country in doc['cameo_operation_countries']:
            if country != "Unknown":
                if doc['cameo_country'] != country:
                    if country not in countries:
                        countries.append(country)
                        
                        y_index = countries.index(country)
                        
                        matrix[x_index][y_index] = matrix[x_index][y_index] + 1
                        
                    else:
                        
                        y_index = countries.index(country)
                        
                        matrix[x_index][y_index] = matrix[x_index][y_index] + 1
                    
                    
header = ["Source_country_cameo_code", "Source_lat", "Source_long", "Targer_country_cameo_code", "Target_lat", "Target_long", "Number_incidents"]


print(len(matrix))
print(len(countries))

             
with open('country_relations_maps.csv', 'w') as fd:
    writer = csv.writer(fd)
    writer.writerow(header)
    
    for row_num in range(len(matrix)):
        for col_num in range(len(matrix)):
            row = []
            row.append(countries[row_num])
            row.append(iso_country_codes_latlong[cameo_iso_country_codes[countries[row_num]]]["lat"])
            row.append(iso_country_codes_latlong[cameo_iso_country_codes[countries[row_num]]]["long"])
            row.append(countries[col_num])
            row.append(iso_country_codes_latlong[cameo_iso_country_codes[countries[col_num]]]["lat"])
            row.append(iso_country_codes_latlong[cameo_iso_country_codes[countries[col_num]]]["long"])
            row.append(matrix[row_num][col_num])
            writer.writerow(row)

