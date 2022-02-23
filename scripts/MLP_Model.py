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
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_GEO_Context_2021_missing
docs = collection.find()

df = pd.DataFrame(list(docs))

dataset = df.values

#Spliting inputs and output variables
firsts = dataset[:, :8]
inputs = dataset[:, 9:]
output = dataset[:, 8:9]

#Transforming inputs(numpy) to Dataframe
inputs_df = pd.DataFrame(data=inputs)

#Selecting positive percentaje and number of incidents in each year as independent variables
inputs = inputs_df.iloc[:, [0,4,5,9,10,14,15,19,20,24,25]]

print(output)
print(inputs)

#Normalizing variables
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
inputs = min_max_scaler.fit_transform(inputs)
output = min_max_scaler.fit_transform(output)

print(output)
print(inputs)

#Spliting into tran, val and test
in_train, in_val_and_test, out_train, out_val_and_test = train_test_split(inputs, output, test_size=0.3)
in_val, in_test, out_val, out_test = train_test_split(in_val_and_test, out_val_and_test, test_size=0.5)

"""

model = Sequential([
    Dense(11, activation=None, input_shape=(in_train.shape[1], )),
    Dense(1, activation='sigmoid'),
])

model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()

hist = model.fit(in_train, out_train,
          batch_size=0, epochs=150,
          validation_data=(in_val, out_val))


print("Model Evaluation")
model.evaluate(in_test, out_test)[1]

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()

"""