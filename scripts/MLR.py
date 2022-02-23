# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

#Multy Layer Perceptron
import pandas as pd
import numpy as np
from pymongo import MongoClient
from sklearn import linear_model
from sklearn import preprocessing

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_GEO_Context_2021_missing
docs = collection.find()
iter_docs = collection.find()

new_collection = db.APT_MLR_Prediction_Results

df = pd.DataFrame(list(docs))

dataset = df.values

#Spliting inputs and output variables
inputs = df.iloc[:, [7,9,13,14,18,19,23,24,28,29,33,34]]
output = df.iloc[:, [8]]

#Data Normalization
#min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
#norm_inputs = min_max_scaler.fit_transform(inputs)
#norm_output = min_max_scaler.fit_transform(output)

regr = linear_model.LinearRegression()
regr.fit(inputs, output)

print(regr.score(inputs, output))

#Normalized Regression
#norm_regr = linear_model.LinearRegression()
#norm_regr.fit(norm_inputs, norm_output)

#Continents List
Europe = ["CAU", "BLK", "CEU", "EEU", "EUR", "MDT", "SCN", "ALA", "ALB", "AND", "AUT", "BLR", "BEL", "BIH", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FRO", "FIN", "FRA", "DEU", "GIB", "GRC", "VAT", "HUN", "ISL", "IRL", "IMY", "ITA", "LVA", "LIE", "LTU", "LUX", "MKD", "MLT", "MDA", "MCO", "MTN", "MSR", "NLD", "NOR", "POL", "PRT", "ROM", "RUS", "SMR", "SRB", "SVK", "SVN", "ESP", "SJM", "SWE", "CHE", "UKR", "GBR"]
Asia = ["WSB", "BAG", "GZS", "ASA", "CAS", "EIN", "MEA", "PGS", "SAS", "SEA", "AFG", "ARM", "AZE", "BHR", "BGD", "BTN", "BRN", "KHM", "CHN", "TMP", "GEO", "HKG", "IND", "IDN", "IRN", "IRQ", "ISR", "JPN", "JOR", "KAZ", "PRK", "KOR", "KWT", "KGZ", "LAO", "LBN", "MAC", "MYS", "MDV", "MNG", "MMR", "NPL", "PSE", "OMN", "PAK", "PHL", "QAT", "SAU", "SGP", "LKA", "SYR", "TJK", "THA", "TUR", "TKM", "ARE", "UZB", "VNM", "YEM"]
Africa = ["AFR", "CFR", "EAF", "NAF", "SAF", "WAF", "DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CMR", "CPV", "CPV", "CAF", "TCD", "COM", "COD", "COG", "CIV", "DJI", "EGY", "ERI", "ETH", "GAB", "GMB", "GHA", "GIN", "GNB", "GNQ", "KEN", "LSO", "LBR", "LBY", "MDG", "MWI", "MLI", "MRT", "MUS", "MYT", "MAR", "MOZ", "NAM", "NER", "NGA", "REU", "RWA", "SHN", "SEN", "SYC", "SLE", "SOM", "ZAF", "ZAF", "SDN", "SWZ", "TZA", "TGO", "TUN", "UGA", "ESH", "ZMB", "ZWE"]
America = ["CRB", "LAM", "NMR", "SAM", "WST", "ASM", "AIA", "ATG", "ARG", "ABW", "BHS", "BRB", "BLZ", "BMU", "BOL", "BRA", "VGB", "CYM", "CHL", "COL", "CAN", "CRI", "CUB", "SLV", "ECU", "DOM", "DMA","FLK", "GUF", "GRL", "GRD", "GLP", "GTM", "GUY", "HTI", "HND", "JAM", "MTQ", "MEX", "ANT", "NIC", "PAN", "PRY", "PER", "PRI", "KNA", "LCA", "SPM", "VCT", "STP", "SUR", "TTO", "TCA", "USA", "VIR", "URY", "VEN"]
Oceania = ["AUS", "COK", "FJI", "PYF", "GUM", "KIR", "MHL", "FSM", "NRU", "NCL", "NZL", "NIU", "NFK", "MNP", "PLW", "PNG", "PCN", "WSM", "SLB", "TKL", "TON", "TUV", "VUT", "WLF"]

dicts = []

errors = []

euro_counter = 0
asia_counter = 0
ame_counter = 0

#Predictions
index = 0
for doc in iter_docs:
    country_1 = doc["country1_code"]
    country_2 = doc["country2_code"]
    incident_year = doc["incident_year"]
    incidents = doc["incidents_0"]
 
    prediction = regr.predict([inputs.iloc[index].values.tolist()])[0][0]
    
    error = abs(output.iloc[index].values.tolist()[0] - regr.predict([inputs.iloc[index].values.tolist()])[0][0])
    
    errors.append(error)
    
    continent_1 = ""
    
    #Continent
    if country_1 in Europe:
        continent_1 = "Europe"
        euro_counter += 1
    elif country_1 in Asia:
        continent_1 = "Asia"
        asia_counter += 1
    elif country_1 in Africa:
        continent_1 = "Africa"
    elif country_1 in America:
        continent_1 = "America"
        ame_counter += 1
    elif country_1 in Oceania:
        continent_1 = "Oceania"
    
    
    dict_doc = {}
    dict_doc["country1_code"] = country_1
    dict_doc["country2_code"] = country_2
    dict_doc["incident_year"] = incident_year
    dict_doc["country1_continent"] = continent_1
    dict_doc["incidents_in_year"] = incidents
    dict_doc["prediction"] = prediction
    dict_doc["prediction_error"] = error
    
    dicts.append(dict_doc)
    
    index+=1

np_errors = np.array(errors)

error_mean = np.mean(np_errors)

print(error_mean)

print(euro_counter)
print(asia_counter)
print(ame_counter)

new_collection.insert_many(dicts)

"""
print("Real Incidents")
print(output.iloc[2].values.tolist()[0])
print("Prediction")
print(regr.predict([inputs.iloc[2].values.tolist()])[0][0])
print("Normalized Prediction")
print(min_max_scaler.inverse_transform([[norm_regr.predict([norm_inputs[2]])[0][0]]])[0][0])

error = abs(output.iloc[2].values.tolist()[0] - regr.predict([inputs.iloc[2].values.tolist()])[0][0])

norm_error = abs(norm_output[2][0] - norm_regr.predict([norm_inputs[2]])[0][0])
norm_error = min_max_scaler.inverse_transform([[norm_error]])[0][0]

print("Prediction Error:")
print(error)
print("Normalized Prediction Error:")
print(norm_error)
"""