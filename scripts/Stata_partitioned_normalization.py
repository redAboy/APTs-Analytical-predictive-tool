# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

#Multy Layer Perceptron
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

df = pd.read_csv("stata_partitioned.csv")

dataset = df.values

#Spliting inputs and output variables
firsts = dataset[:, :3]
inputs = dataset[:, 3:7]
output = dataset[:, 7:8]

print(inputs)

#Normalizing variables
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
inputs = min_max_scaler.fit_transform(inputs)
output = min_max_scaler.fit_transform(output)

firsts_df = pd.DataFrame(firsts)
inputs_df = pd.DataFrame(inputs)
output_df = pd.DataFrame(output)

pd.concat([firsts_df, inputs_df, output, df], axis=1).to_csv("stat_partitioned_normalized.csv", index=False)