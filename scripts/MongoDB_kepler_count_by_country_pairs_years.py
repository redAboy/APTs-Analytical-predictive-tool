# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Total_incidents_by_country_pairs_years_table
docs = collection.find()

new_collection = db.Kepler_APT_Total_incidents_by_country_pairs_years_table

general = {}

headers = []

field_names= []

for header in docs[0].keys():
    
    if header != "_id":
        field_dict = {}
        field_dict["name"] = header
        field_names.append(header)
        #Format
        if header == "country1_latitude":
            field_dict["format"] = ""
            field_dict["type"] = "real"
        elif header == "country1_longitude":
            field_dict["format"] = ""
            field_dict["type"] = "real"
        elif header == "country2_latitude":
            field_dict["format"] = ""
            field_dict["type"] = "real"
        elif header == "country2_longitude":
            field_dict["format"] = ""
            field_dict["type"] = "real"
        elif header == "year":
            field_dict["format"] = "YYYY"
            field_dict["type"] = "timestamp"
        elif header == "incidents":
            field_dict["format"] = ""
            field_dict["type"] = "integer"
        else:
            field_dict["format"] = ""
            field_dict["type"] = "string"
            
        headers.append(field_dict)
        

rows = []

for doc in docs:
    
    row = []
    
    for field in field_names:
        
        if field == "country1_latitude":
            row.append(float(doc[field]))
        elif field == "country1_longitude":
            row.append(float(doc[field]))
        elif field == "country2_latitude":
            row.append(float(doc[field]))
        elif field == "country2_longitude":
            row.append(float(doc[field]))
        else:
            try:
                row.append(doc[field])
            except:
                row.append("")
            
    rows.append(row)
    
general["fields"] = headers
general["rows"] = rows


new_collection.insert_one(general)           



