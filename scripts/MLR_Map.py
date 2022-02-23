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
import json

with open ("cameo_to_iso3166.json", "r") as fd_out:
    cameo_iso_country_codes = json.load(fd_out)
    
#Iso country lat and longs loading
with open ("countrycode-latlong.json", "r") as fd_out:
    iso_country_codes_latlong = json.load(fd_out)

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_GEO_Context_2021_missing
docs = collection.find()
iter_docs = collection.find()

new_collection = db.APT_MLR_Prediction_Results_Map

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

dicts = []

errors = []

#Predictions
index = 0
for doc in iter_docs:
    country_1 = doc["country1_code"]
    country1_lat = iso_country_codes_latlong[cameo_iso_country_codes[country_1]]["lat"]
    country1_long = iso_country_codes_latlong[cameo_iso_country_codes[country_1]]["long"]
    country_2 = doc["country2_code"]
    country2_lat = iso_country_codes_latlong[cameo_iso_country_codes[country_2]]["lat"]
    country2_long = iso_country_codes_latlong[cameo_iso_country_codes[country_2]]["long"]
    incident_year = doc["incident_year"]
    incidents = doc["incidents_0"]
 
    prediction = regr.predict([inputs.iloc[index].values.tolist()])[0][0]
    
    error = abs(output.iloc[index].values.tolist()[0] - regr.predict([inputs.iloc[index].values.tolist()])[0][0])
    
    errors.append(error)
    
    dict_doc = {}
    dict_doc["country1_code"] = country_1
    dict_doc["latitude_1"] = country1_lat
    dict_doc["longitude_1"] = country1_long 
    dict_doc["country2_code"] = country_2
    dict_doc["latitude_2"] = country2_lat
    dict_doc["longitude_2"] = country2_long 
    dict_doc["incident_year"] = incident_year
    dict_doc["incidents_in_year"] = incidents
    dict_doc["prediction"] = prediction
    dict_doc["prediction_error"] = error
    
    dicts.append(dict_doc)
    
    index+=1

np_errors = np.array(errors)

error_mean = np.mean(np_errors)

print(error_mean)

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