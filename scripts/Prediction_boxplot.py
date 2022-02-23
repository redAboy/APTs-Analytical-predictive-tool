# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

#Multy Layer Perceptron
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
from pymongo import MongoClient


client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_MLR_Prediction_Results
docs = collection.find()

df = pd.DataFrame(list(docs))

df = df.iloc[:, 1:]

x = 'country1_continent'
y = 'prediction_error'

#Chart
plt.figure(figsize=(20,10,))
ax = sea.boxplot(x=x, y=y, data=df, palette="rocket")
ax = sea.swarmplot(x=x, y=y, data=df, color='grey')

plt.show()






