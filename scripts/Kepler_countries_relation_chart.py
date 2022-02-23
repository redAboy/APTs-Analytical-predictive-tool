# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""


import csv

import matplotlib.pyplot as plt
#Mongodb Atlas
from pymongo import MongoClient

from chord import Chord

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
                if country not in countries:
                    countries.append(country)
                    
                    y_index = countries.index(country)
                    
                    matrix[x_index][y_index] = matrix[x_index][y_index] + 1
                    
                else:
                    
                    y_index = countries.index(country)
                    
                    matrix[x_index][y_index] = matrix[x_index][y_index] + 1
                    
                    
Chord(matrix, countries).to_html("out.html")
                    
                    
"""Write results in file
with open('countries_relationship.csv', 'w') as fd:
    writer = csv.writer(fd)
    writer.writerow(countries)
    for row in range(len(countries)):
        writer.writerow(matrix[row])
"""
    
