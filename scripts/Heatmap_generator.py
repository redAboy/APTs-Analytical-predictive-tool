# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:36:16 2021

@author: QWERTY
"""

from pymongo import MongoClient
import csv

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_MLR_Prediction_Results


header = ['', 'RUS', 'BEL', 'UKR', 'BLR', 'GBR', 'IRN', 'PRK', 'IND', 'KHM', 'CHN', 'JPN', 'KOR', 'SAU', 'AFG', 'VNM', 'PAK', 'SAS', 'ARE', 'GEO', 'MEA', 'AZE', 'SYR', 'TUR', 'KAZ', 'USA', 'COL', 'ARG', 'BRA', 'AUS']

attacking_countries_order = ['RUS', 'BEL', 'UKR', 'BLR', 'GBR', 'IRN', 'PRK', 'IND', 'KHM', 'CHN', 'JPN', 'KOR', 'SAU', 'AFG', 'VNM', 'PAK', 'SAS', 'ARE', 'GEO', 'MEA', 'AZE', 'SYR', 'TUR', 'KAZ', 'USA', 'COL', 'ARG', 'BRA', 'AUS']

affected_countries_order = ['GBR', 'BEL', 'POL', 'FIN', 'FRA', 'IRL', 'NOR', 'SWE', 'ESP', 'DEU', 'GRC', 'ITA', 'CHE', 'DNK', 'EST', 'AUT', 'UKR', 'BGR', 'ALB', 'BLR', 'CYP', 'NLD', 'RUS', 'LVA', 'HRV', 'ISR', 'JOR', 'CHN', 'JPN', 'SAU', 'SGP', 'IDN', 'IND', 'MYS', 'OMN', 'PHL', 'THA', 'TUR', 'BGD', 'MDV', 'PAK', 'AFG', 'ARE', 'QAT', 'BHR', 'KWT', 'LBN', 'IRQ', 'MMR', 'MNG', 'GEO', 'KHM', 'NPL', 'KAZ', 'ARM', 'YEM', 'AZE', 'TJK', 'TKM', 'LKA', 'UZB', 'MLI', 'ZAF', 'ZAF', 'EGY', 'KEN', 'RWA', 'SDN', 'NER', 'NGA', 'SOM', 'CAN', 'USA', 'BRA', 'CUB', 'MEX', 'ARG', 'PER', 'COL', 'ECU', 'CHL', 'GTM', 'AUS', 'NZL']

with open("heatmap_final.csv", 'w') as f:
    
    writer = csv.writer(f, delimiter=';')
    
    writer.writerow(header)
    
    for country_row in affected_countries_order:
        
        row_list = []
        row_list.append(country_row)
        
        for country_col in attacking_countries_order:
            
            found = False
            
            acumulated_error = 0
                
            prediction_counter = 0
            
            docs = collection.find()
            
            for doc in docs:

                if doc["country2_code"] == country_row and doc["country1_code"] == country_col:
                    acumulated_error += doc["prediction_error"]
                    prediction_counter += 1
                    found = True
            
            error_mean = 0
                
            if found:
                error_mean = acumulated_error/prediction_counter
                
            error_mean = str(error_mean).replace(".", ",")
                    
            row_list.append(error_mean)
            
        writer.writerow(row_list)
                
        

    