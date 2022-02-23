# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

#Charts
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime


#Mongodb Atlas
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents

collection_docs = collection.find()

dates = []
group_names = []

for doc in collection_docs:
    try:
        date = doc["operation_month"] + " " + doc["operation_year"]
        dates.append(datetime.strptime(date, '%b %Y'))
    except:
        continue
        
    group_names.append(doc["group_name"])

# Choose some nice levels
levels = np.tile([-79, 79, -77, 77, -75, 75, -73, 73, -71, 71, -69, 69, -67, 67, -65, 65, -63, 63, -61, 61, -59, 59, -57, 57, -55, 55, -53, 53, -51, 51, -49, 49, -47, 47, -45, 45, -43, 43, -41, 41, -39, 39, -37, 37, -35, 35, -33, 33, -31, 31, -29, 29, -27, 27, -25, 25, -23, 23, -21, 21, -19, 19, -17, 17, -15, 15, -13, 13, -11, 11, -9, 9, -7, 7, -5, 5, -3, 3, -1, 1], int(np.ceil(len(dates)/80)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(400.6, 50), constrained_layout=True)
ax.set(title="APTs Incidents")

markerline, stemline, baseline = ax.stem(dates, levels,
                                         linefmt="C3-", basefmt="k-",
                                         use_line_collection=True)

plt.setp(markerline, mec="k", mfc="w", zorder=3)

# Shift the markers to the baseline by replacing the y-data by zeros.
markerline.set_ydata(np.zeros(len(dates)))

# annotate lines
vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
for d, l, r, va in zip(dates, levels, group_names, vert):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                textcoords="offset points", va=va, ha="right")
    
# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=90, ha="right")

# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)
    
ax.margins(y=0.1)

fname = "Timeline.png"

plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
    