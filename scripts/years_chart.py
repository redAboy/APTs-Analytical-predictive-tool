# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

import numpy as np
import matplotlib.pyplot as plt
#Mongodb Atlas
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents

collection_docs = collection.find()

years = {}

for doc in collection_docs:
    
    if doc["operation_year"] in years:
        years[doc["operation_year"]] = years[doc["operation_year"]] + 1
    else:
        years[doc["operation_year"]] = 1
        
height = []
bars = []
first = 1996
for year in years:
    if year.isdigit():
        # Create dataset
        bars.append(int(year))
        
bars.sort()

for bar in bars:
    height.append(int(years[str(bar)]))

print(height)
print(bars)

# Figure Size
fig, ax = plt.subplots(figsize =(16, 8))
 
# Horizontal Bar Plot
ax.barh(bars, height)
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 1)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 12, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title("APT's Incidents by Years",
             loc ='left', )
 
# Add Text watermark
fig.text(0.9, 0.15, '', fontsize = 14,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)
 
# Show Plot
plt.show()
