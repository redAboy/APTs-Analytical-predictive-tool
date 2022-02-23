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
stats_collection = db.APT_Total_incidents_by_country_pairs_years

collection_docs = collection.find()
stats_collection_docs = stats_collection.find_one()

df = pd.DataFrame([], columns= ["Contry1", "Country2", "Year", "Positive_Goldsteins", "Negative_Goldsteins", "Goldstein_mean", "Goldstein_std", "Number_of_Incidents"])

for doc in collection_docs:
    country_1 = doc["country1_code"]
    country_2 = doc["country2_code"]
    year = int(doc["incident_year"])
    for year_tag in range (0, 6):
        
        df_list = []
        
        current_year = year-year_tag
        tag = str(year_tag)
        
        query = str(current_year)+"_"+country_1+"_"+country_2
        
        try:
            stat = stats_collection_docs[query]
        except:
            stat = 0
        
        
        #Insert into dataframe
        df_list.append(country_1)
        df_list.append(country_2)
        df_list.append(str(current_year))
        df_list.append(doc["positive_goldstein_mentions_"+tag])
        df_list.append(doc["negative_goldstein_mentions_"+tag])
        df_list.append(doc["golds_mean_"+tag])
        df_list.append(doc["golds_std_"+tag])
        df_list.append(stat)
        
        df.loc[len(df)] = df_list
        

df.to_csv('stata_partitionate.csv', index=False)