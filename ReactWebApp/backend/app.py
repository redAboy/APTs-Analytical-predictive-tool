from flask import Flask, json, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
import pymongo
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
from urllib.parse import urlparse

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE'
mongo = PyMongo(app)

CORS(app)

"""Raw Data"""

@app.route('/rawdata/test', methods=['GET'])
def dbtojson():
    db = mongo.db.test
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'group_name': doc['group_name'],
            'group_country': doc['group_country'],
            'reference': doc['reference'], 
            'operation_date': doc['operation_date'],
            'operation_month': doc['operation_month'],
            'operation_year': doc['operation_year'],
            'operation_description': doc['operation_description'],
            'operation_urls': doc['operation_urls'],
            'operation_countries': doc['operation_countries'],
        })
    return jsonify(docs)


@app.route('/rawdata/APT_GEO_Context_2021_missing', methods=['GET'])
def APT_GEO_Context_2021_missingtojson():
    db = mongo.db.APT_GEO_Context_2021_missing
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country1_code': doc['country1_code'],
            'country2_code': doc['country2_code'],
            'incident_id': str(ObjectId(doc['incident_id'])),
            'incident_year': doc['incident_year'],
            'country1_snt_incidents': doc['country1_snt_incidents'],
            'contry2_rvd_incidents': doc['contry2_rvd_incidents'],
            'country1_to_country2_incidents': doc['country1_to_country2_incidents'],
            'incidents_0': doc['incidents_0'],
            'positive_goldstein_mentions_0': doc['positive_goldstein_mentions_0'],
            'negative_goldstein_mentions_0': doc['negative_goldstein_mentions_0'],
            'golds_mean_0': doc['golds_mean_0'],
            'golds_std_0': doc['golds_std_0'],
            'incidents_1': doc['incidents_1'],
            'positive_goldstein_mentions_1': doc['positive_goldstein_mentions_1'],
            'negative_goldstein_mentions_1': doc['negative_goldstein_mentions_1'],
            'golds_mean_1': doc['golds_mean_1'],
            'golds_std_1': doc['golds_std_1'],
            'incidents_2': doc['incidents_2'],
            'positive_goldstein_mentions_2': doc['positive_goldstein_mentions_2'],
            'negative_goldstein_mentions_2': doc['negative_goldstein_mentions_2'],
            'golds_mean_2': doc['golds_mean_2'],
            'golds_std_2': doc['golds_std_2'],
            'incidents_3': doc['incidents_3'],
            'positive_goldstein_mentions_3': doc['positive_goldstein_mentions_3'],
            'negative_goldstein_mentions_3': doc['negative_goldstein_mentions_3'],
            'golds_mean_3': doc['golds_mean_3'],
            'golds_std_3': doc['golds_std_3'],
            'incidents_4': doc['incidents_4'],
            'positive_goldstein_mentions_4': doc['positive_goldstein_mentions_4'],
            'negative_goldstein_mentions_4': doc['negative_goldstein_mentions_4'],
            'golds_mean_4': doc['golds_mean_4'],
            'golds_std_4': doc['golds_std_4'],
            'incidents_5': doc['incidents_5'],
            'positive_goldstein_mentions_5': doc['positive_goldstein_mentions_5'],
            'negative_goldstein_mentions_5': doc['negative_goldstein_mentions_5'],
            'golds_mean_5': doc['golds_mean_5'],
            'golds_std_5': doc['golds_std_5']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_GEO_Context_complete', methods=['GET'])
def APT_GEO_Context_completetojson():
    db = mongo.db.APT_GEO_Context_complete
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country1_code': doc['country1_code'],
            'country2_code': doc['country2_code'],
            'incident_id': str(ObjectId(doc['incident_id'])),
            'incident_year': doc['incident_year'],
            'country1_snt_incidents': doc['country1_snt_incidents'],
            'contry2_rvd_incidents': doc['contry2_rvd_incidents'],
            'country1_to_country2_incidents': doc['country1_to_country2_incidents'],
            'incidents_0': doc['incidents_0'],
            'positive_goldstein_mentions_0': doc['positive_goldstein_mentions_0'],
            'negative_goldstein_mentions_0': doc['negative_goldstein_mentions_0'],
            'golds_mean_0': doc['golds_mean_0'],
            'golds_std_0': doc['golds_std_0'],
            'incidents_1': doc['incidents_1'],
            'positive_goldstein_mentions_1': doc['positive_goldstein_mentions_1'],
            'negative_goldstein_mentions_1': doc['negative_goldstein_mentions_1'],
            'golds_mean_1': doc['golds_mean_1'],
            'golds_std_1': doc['golds_std_1'],
            'incidents_2': doc['incidents_2'],
            'positive_goldstein_mentions_2': doc['positive_goldstein_mentions_2'],
            'negative_goldstein_mentions_2': doc['negative_goldstein_mentions_2'],
            'golds_mean_2': doc['golds_mean_2'],
            'golds_std_2': doc['golds_std_2'],
            'incidents_3': doc['incidents_3'],
            'positive_goldstein_mentions_3': doc['positive_goldstein_mentions_3'],
            'negative_goldstein_mentions_3': doc['negative_goldstein_mentions_3'],
            'golds_mean_3': doc['golds_mean_3'],
            'golds_std_3': doc['golds_std_3'],
            'incidents_4': doc['incidents_4'],
            'positive_goldstein_mentions_4': doc['positive_goldstein_mentions_4'],
            'negative_goldstein_mentions_4': doc['negative_goldstein_mentions_4'],
            'golds_mean_4': doc['golds_mean_4'],
            'golds_std_4': doc['golds_std_4'],
            'incidents_5': doc['incidents_5'],
            'positive_goldstein_mentions_5': doc['positive_goldstein_mentions_5'],
            'negative_goldstein_mentions_5': doc['negative_goldstein_mentions_5'],
            'golds_mean_5': doc['golds_mean_5'],
            'golds_std_5': doc['golds_std_5']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Group_Incidents', methods=['GET'])
def APT_Group_Incidentstojson():
    db = mongo.db.APT_Group_Incidents
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'group_name': doc['group_name'],
            'group_country': doc['group_country'],
            'reference': doc['reference'],
            'operation_date': doc['operation_date'],
            'operation_month': doc['operation_month'],
            'operation_year': doc['operation_year'],
            'operation_description': doc['operation_description'],
            'operation_urls': doc['operation_urls'],
            'operation_countries': doc['operation_countries']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Group_Incidents_CAMEO', methods=['GET'])
def APT_Group_Incidents_CAMEOtojson():
    db = mongo.db.APT_Group_Incidents_CAMEO
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'group_name': doc['group_name'],
            'group_country': doc['group_country'],
            'reference': doc['reference'],
            'operation_date': doc['operation_date'],
            'operation_month': doc['operation_month'],
            'operation_year': doc['operation_year'],
            'operation_description': doc['operation_description'],
            'operation_urls': doc['operation_urls'],
            'operation_countries': doc['operation_countries'],
            'cameo_country': doc['cameo_country'],
            'cameo_operation_countries': doc['cameo_operation_countries']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Total_incidents_by_country_pairs_years_table', methods=['GET'])
def APT_Total_incidents_by_country_pairs_years_tabletojson():
    db = mongo.db.APT_Total_incidents_by_country_pairs_years_table
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'year': doc['year'],
            'country1': doc['country1'],
            'country1_code': doc['country1_code'],
            'country1_latitude': doc['country1_latitude'],
            'country1_longitude': doc['country1_longitude'],
            'country2': doc['country2'],
            'country2_code': doc['country2_code'],
            'country2_latitude': doc['country2_latitude'],
            'country2_longitude': doc['country2_longitude'],
            'incidents': doc['incidents']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Total_incidents_by_country_pairs_table', methods=['GET'])
def APT_Total_incidents_by_country_pairs_tabletojson():
    db = mongo.db.APT_Total_incidents_by_country_pairs_table
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country1': doc['country1'],
            'country1_code': doc['country1_code'],
            'country1_latitude': doc['country1_latitude'],
            'country1_longitude': doc['country1_longitude'],
            'country2': doc['country2'],
            'country2_code': doc['country2_code'],
            'country2_latitude': doc['country2_latitude'],
            'country2_longitude': doc['country2_longitude'],
            'incidents': doc['incidents']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Total_incident_sent_by_country_table', methods=['GET'])
def APT_Total_incident_sent_by_country_tabletojson():
    db = mongo.db.APT_Total_incident_sent_by_country_table
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country': doc['country'],
            'country_code': doc['country_code'],
            'latitude': doc['latitude'],
            'longitude': doc['longitude'],
            'incidents_sent': doc['incidents_sent']
        })
    return jsonify(docs)

@app.route('/rawdata/APT_Total_incidents_sent_by_years_table', methods=['GET'])
def APT_Total_incidents_sent_by_years_tabletojson():
    db = mongo.db.APT_Total_incidents_sent_by_years_table
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'year': doc['year'],
            'country': doc['country'],
            'country_code': doc['country_code'],
            'latitude': doc['latitude'],
            'longitude': doc['longitude'],
            'incidents': doc['incidents']
        })
    return jsonify(docs)


@app.route('/rawdata/APT_Total_incident_received_by_country_table', methods=['GET'])
def APT_Total_incident_received_by_country_tabletojson():
    db = mongo.db.APT_Total_incident_received_by_country_table
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country': doc['country'],
            'country_code': doc['country_code'],
            'latitude': doc['latitude'],
            'longitude': doc['longitude'],
            'incidents_received': doc['incidents_received']
        })
    return jsonify(docs)

@app.route('/rawdata/APT_Total_incident_by_group', methods=['GET'])
def APT_Total_incident_by_grouptojson():
    db = mongo.db.APT_Total_incident_by_group
    docs = []
    for doc in db.find():
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'group_name': doc['group_name'],
            'country': doc['country'],
            'country_code': doc['country_code'],
            'latitude': doc['latitude'],
            'longitude': doc['longitude'],
            'incidents_sent': doc['incidents_sent'],
            'year_list': doc['year_list']
        })
    return jsonify(docs)

@app.route('/rawdata/topthreats', methods=['GET'])
def topthreats():
    db = mongo.db.APT_Total_incident_sent_by_country_table
    docs = []
    for doc in db.find().sort('incidents_sent', pymongo.DESCENDING).limit(4):
        docs.append({
            '_id': str(ObjectId(doc['_id'])),
            'country': doc['country'],
            'country_code': doc['country_code'],
            'latitude': doc['latitude'],
            'longitude': doc['longitude'],
            'incidents_sent': doc['incidents_sent']
        })
    return jsonify(docs)









"""Analytics"""

"""Headers"""

@app.route('/analytics/APT_GEO_Context_2021_missing', methods=['GET'])
def APT_GEO_Context_2021_missing_headertojson():
    db = mongo.db.APT_GEO_Context_2021_missing
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)

@app.route('/analytics/APT_GEO_Context_complete', methods=['GET'])
def APT_GEO_Context_complete_headertojson():
    db = mongo.db.APT_GEO_Context_complete
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)

@app.route('/analytics/APT_Group_Incidents', methods=['GET'])
def APT_Group_Incidents_headertojson():
    db = mongo.db.APT_Group_Incidents
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Group_Incidents_CAMEO', methods=['GET'])
def APT_Group_Incidents_CAMEO_headertojson():
    db = mongo.db.APT_Group_Incidents_CAMEO
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incidents_by_country_pairs_years_table', methods=['GET'])
def APT_Total_incidents_by_country_pairs_years_table_headertojson():
    db = mongo.db.APT_Total_incidents_by_country_pairs_years_table
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incidents_by_country_pairs_table', methods=['GET'])
def APT_Total_incidents_by_country_pairs_table_headertojson():
    db = mongo.db.APT_Total_incidents_by_country_pairs_table
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incident_sent_by_country_table', methods=['GET'])
def APT_Total_incident_sent_by_country_table_headertojson():
    db = mongo.db.APT_Total_incident_sent_by_country_table
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incidents_sent_by_years_table', methods=['GET'])
def APT_Total_incidents_sent_by_years_table_headertojson():
    db = mongo.db.APT_Total_incidents_sent_by_years_table
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incident_received_by_country_table', methods=['GET'])
def APT_Total_incident_received_by_country_table_headertojson():
    db = mongo.db.APT_Total_incident_received_by_country_table
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)


@app.route('/analytics/APT_Total_incident_by_group', methods=['GET'])
def APT_Total_incident_by_group_headertojson():
    db = mongo.db.APT_Total_incident_by_group
    doc = db.find_one()
    keys = []
    for key in doc.keys():
        if key != '_id':
            keys.append(key)
    response = {}
    response['headers'] = keys
    return jsonify(response)




"""Data"""

@app.route('/analysis/<parameters>', methods=['GET'])
def queryCollection(parameters):

    #Get collection
    collection = parameters.split('&')[0].split("=")[1]
    db = mongo.db[collection]
    query = {}
    query_list = []
    for param in parameters.split('&')[1:]:
        key = param.split("=")[0]
        value = param.split("=")[1]
        query_list.append({key:value})
    query['$and'] = query_list
    docs = db.find(query, {'_id': False, 'incident_id': False})
    doc_list = list(docs)

    return jsonify(doc_list)




"""Maps"""

@app.route('/maps/APT_Total_incident_sent_by_group', methods=['GET'])
def Kepler_APT_Total_incident_sent_by_group():
    db = mongo.db.Kepler_APT_Total_incident_sent_by_group
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)


@app.route('/maps/APT_Total_incident_sent_by_country', methods=['GET'])
def Kepler_APT_Total_incident_sent_by_country():
    db = mongo.db.Kepler_APT_Total_incident_sent_by_country
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)


@app.route('/maps/APT_Total_incident_received_by_country', methods=['GET'])
def Kepler_APT_Total_incident_received_by_country():
    db = mongo.db.Kepler_APT_Total_incident_received_by_country
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)

@app.route('/maps/APT_Total_incident_sent_by_years', methods=['GET'])
def Kepler_APT_Total_incident_sent_by_years():
    db = mongo.db.Kepler_APT_Total_incident_sent_by_years
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)


@app.route('/maps/APT_Total_incidents_by_country_pairs_table', methods=['GET'])
def Kepler_APT_Total_incidents_by_country_pairs_table():
    db = mongo.db.Kepler_APT_Total_incidents_by_country_pairs_table
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)


@app.route('/maps/APT_Total_incidents_by_country_pairs_years_table', methods=['GET'])
def Kepler_APT_Total_incidents_by_country_pairs_years_table():
    db = mongo.db.Kepler_APT_Total_incidents_by_country_pairs_years_table
    docs = {}
    for doc in db.find():
        docs["fields"] = doc['fields']
        docs["rows"] = doc['rows']
    return jsonify(docs)




"""Prediction"""
@app.route('/prediction/<country1_code>/<country2_code>/<year>', methods=['GET'])
def Prediction(country1_code, country2_code, year):
    result = {}

    last_collection_year = 2020

    attacking_countries = ["RUS","BEL","UKR","BLR","GBR","IRN","PRK","IND","KHM","CHN","JPN","KOR","SAU","AFG","VNM","PAK","SAS","ARE","GEO","MEA","AZE","SYR","TUR","KAZ","USA","COL","ARG","BRA","AUS"]
    affected_countries = ["GBR","BEL","POL","FIN","FRA","IRL","NOR","SWE","ESP","DEU","GRC","ITA","CHE","DNK","EST","AUT","UKR","BGR","ALB","BLR","CYP","NLD","RUS","LVA","HRV","ISR","JOR","CHN","JPN","SAU","SGP","IDN","IND","MYS","OMN","PHL","THA","TUR","BGD","MDV","PAK","AFG","ARE","QAT","BHR","KWT","LBN","IRQ","MMR","MNG","GEO","KHM","NPL","KAZ","ARM","YEM","AZE","TJK","TKM","LKA","UZB","MLI","ZAF","ZAF","EGY","KEN","RWA","SDN","NER","NGA","SOM","CAN","USA","BRA","CUB","MEX","ARG","PER","COL","ECU","CHL","GTM","AUS","NZL"]
    deviation_matrix = [[4.600960277,0,1.040260926,0.99717337,0,0.655272933,4.48084003,0,0,1.808328223,0.396049,0,0.037623225,0,2.019019325,0.552245956,0.00507842,0,0,0,0,0,0,0,0,0,0,0,0],[0.647488014,0,0,0,0,0.425968869,0,0,0,0.771027255,0,0.205745056,0,0,0.563465048,0,0,0,0,0,0,0,0.350942501,0,1.935001361,0,0,0,0],[1.715215665,0,0,0,0,0,1.501483858,0,0,3.235722806,0,0,0,1.387871379,0.959439081,0.188023972,0,0,0,0,0,0,0.821777986,0,0,0,0,0,0],[0.216308962,0,0,0,0,0,0.739993825,0,0,4.458546851,0.29308235,0,0,0,0.121245789,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.135995647,0,0.109606763,0,0,0.972005992,3.673683148,0,0,1.846077118,0.382622801,0,0.354417735,0,1.624193703,0,0,0,0,0,0,1.117710122,0.131313198,0,1.336284992,0,0,0.112209855,0],[2.154411775,0,0,0,0.205745056,0,0,0,0,0.967469916,0,0,0,0,0.776505202,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2.582533022,0,0,0,0,0,0,0,0,1.086691839,0,0,0,0,0.285300242,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[3.505318697,0.237464234,0,0,0,0,0,0,0,0.713366418,0.099137074,0,0,0,0.032343496,0,0,0,0,0,0,0,1.044793628,0,0.132211401,0,0,0,0],[0.393984774,0,0.35772902,0,0,0.788433356,2.680495843,0,0,0.535090041,0,0,0.528696963,0,0.477395485,0.50683026,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.205313417,0,0.407195495,0,0,0.385611164,3.000609659,0,0,1.769862085,1.056509699,0.014855908,0.10682285,0,0.289556297,2.749300305,0,0,0,0,0,0,1.314609371,0,0,0,0,0,0],[0,0,0,0,0,0.445868364,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.282516432,0,1.204375213,0.147619455,0,0.874589172,0.125957803,0,0,0.519904811,0,0.34215372,0.212506394,0,1.088187457,0,0,0,0,0,0,0,0.731437074,0,1.710487351,0,0,0,0],[0.225638138,0,0,0,0,0,0,0,0,1.457966345,1.051840633,0,0,0,0,0.546135317,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.820044744,0,0,0,0,0,0,0,0,2.49736661,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[6.408096749,0,0.619144168,0,0,1.341330022,0,0,0,0.833940683,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.682660422,0,0,0,0],[1.222149153,0,0,0,0,0,0,0,0,1.436679624,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1.132037778,1.315649297,0,0,0,0,0,0,0,0,0.5550633,0,0,0,0,0,0,0.851078881,0,0.960931743,0,0,0,0],[1.027079339,0,0,0,0,0,0.132211401,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.058677747,0,0,0,0],[0.995404498,0,0,0,0,0,0,0,0,1.095427215,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2.480425879,0,0,0,0,0,0,0,0,0.58884779,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.205745056,0,0,0,0],[1.779089628,0,0,0,0,0,0,0,0,0.031211036,0,0,0,0,0,1.24542223,0,0,0,0,0,0,1.979673056,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1.073793041,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,2.242352887,0,0,0,0.936382583,0,0,1.145404946,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.692145869,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.115473093,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2.483869204,0,0.569459887,0,0,2.466634995,0.622429537,0,0,0.856692912,0,0,0.510097549,0.980017732,0,0,0,0,0,0,0,0,0.259175191,0,1.629353739,0,0,0,1.747374439],[1.470559495,0,0,0,0,1.86956438,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2.362136154,0,0,0,0],[1.207192255,0.180602281,0,0.175226189,0,0.529591489,1.678103573,0.427972129,0.090071267,0,0.898556746,1.632095434,0.639646869,0,1.92524902,1.422755033,1.331268401,0.145113945,0,0,0,0.311159062,0.540100115,0,1.132289754,0,0,0,1.393403806],[0.302606056,0,0.151507582,0,0,5.140539057,2.112933572,1.292535289,0.966916639,4.452878661,0,0.584763137,0.274881562,0,1.105822626,2.480747671,0,0,0,0,0,0,0.825313678,0,1.102010853,0,0.858810131,0,0],[0.231263422,0,0,0,0,5.687419797,0,0,0,1.353235448,1.08901022,0,0,0,0,0.020286078,0.385098514,1.519722068,0,0,0,0,1.455053984,0,2.829141784,0,0,0,0],[4.103111039,0,0,0,0,0.76885222,0.271937521,0,0,3.747112857,0,0.205745056,0,0,0.586687629,0.359110122,0,0,0,0,0,0,0.436780419,0,0,0,0.063039915,0,0],[1.364077516,0,0,0,0,0,0,0,0,1.804360522,0,0.205745056,0,0,0.006307394,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[6.256912268,0,0.60117758,0,0,1.257038905,0.247392785,0,1.667411828,1.964647557,0.417329313,0.014855908,0.01450405,0.065458172,1.893002213,4.121261576,1.023093032,0,0,0.217662474,0,0.220542971,0.356371593,0,1.418320142,0,0,0.002789547,0],[2.984844549,0,0,0,0,0,0,0,0,3.140303723,0,0,0,1.118522077,0.334724489,0.354799847,0,0,0,0,0,0,0.494094859,0,0,0,0,0,0],[0.446452052,0,0,0,0,0.237979762,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.279077355,0,0,0,0,0,0,0,0.13004293,1.615474636,0,0.205745056,0,0.931177657,0.799564568,1.076529982,0,0,0,0,0,0,0.765809407,0,0,0,0,0,0],[1.313471236,0,0,0,0,0,0,0,0,0.965122136,0,0,0,0,1.565092072,0,0,0.720221829,0,0,0,0,0,0,0,0,0,0,0],[0.824262813,0,0,0,0.205745056,4.721874393,0,0,0,0.570345082,0,0,0,0.406941375,1.113805278,0.23370374,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.657993135,0,0.117600132,0,2.113464043,0,0,0,0.992359439,0,0,0,0,0,0,1.588297817,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.236246485,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.88416704,0,0,0,0,1.851626228,0.296785725,0.84466571,0,0,0,0.205745056,0,0.702614429,0,0,1.811914251,0,0,4.468644174,0,0,0.737034608,0,1.391739908,0,0,0,0],[1.988251066,0,0,0,0,2.708212001,0,0.67961397,0.718021117,0.923620228,0,0,0,0,1.761095556,1.53087945,0,0,0,0,0,0,1.260401187,0,0,0,0,0,0],[1.1339453,0,0,0,0,2.760061385,2.434475956,0,0,0,0.078452297,0.205745056,0,0,0,0,0,0,0,0,0,0,0,0,0.843798189,0,0,0.155670755,0],[0,0,0,0,0,0,0,0,0,0.775617587,0,0,0,0,0,0,0,0.159608844,0,0,0,0,0.220990171,0,0,0,0,0,0],[0,0,0,0,0,1.005318535,0,0,0,0,0,0,0,0,0,0,0,0.081450827,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,2.096604353,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.008492049,0,0,0,0,1.614300652,0,0,0,0,0,0,0,0.332385079,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.38252418,0,0,0,0,1.187967406,0,0,0,1.485156581,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1.776246412,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.280180958,0,0.63665237,0,0,0,0.777090882,0,0,0,0,0,0,1.104552309,0,0,0,0,0,0],[2.914909451,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1.169073331,0,0,0,0,0.561228189,0.38853109,0,0,0,0,0,0,1.008446226,0,0,0,0,0,0],[1.197458668,0,0,0,0,0,0,0,0,0.593965555,0,0,0,0,0.949873356,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.766031012,0,0.205745056,0,0,0,0.040678676,0,0,0,0,0,0,0,0,0.205745056,0,0,0,0],[0.127391691,0,0,0,0,0,0,0,0,0.002134934,0,0,0,0,0,0,0,0,0,0,2.577522413,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.132211401,0,0,0,0],[0.25364126,0,0,0,0,0,0,0,0,0.264739259,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.236186012,0,0,0,0,0,0,0,0,2.649929318,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.146463981,0,0,0,0,0,0],[0.119967009,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.908234058,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2.741170954,0,0,0,0,0.336704411,0,0,1.492575931,0.375847944,0,0,0,1.108098298,0,0.325413717,0,0,0,0,0,0,0,0,1.969496596,0,0,0,0],[1.991700923,0,0,0,0.205745056,0,2.271010803,0,0,0.461235869,0,0,0,0,2.351355317,0,0,0,0,0,0,0,0,0,0.899245303,0,0,0,0],[1.991700923,0,0,0,0.205745056,0,2.271010803,0,0,0.461235869,0,0,0,0,2.351355317,0,0,0,0,0,0,0,0,0,0.899245303,0,0,0,0],[0,0,0,0,0,0.796850224,0,0,0,0,0,0,0,0.576818614,0,0,0,0,0,0,0,0,1.091078182,0,0.014855908,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.014855908,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0.084755183,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.614450513,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,3.487678298,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.199082676,0,0,0,0,0,0.006479678,0,0,2.244647375,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.157378512,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.614397777,0,0,0,0],[3.032619964,0,0.723989621,0,0,2.070049452,0.916886567,0,0,0.987457787,0.36546402,2.151547094,0,0,0.159132859,0,0,0.120128952,0,0,0,1.209371774,0.532523973,0,0,0,0.823149198,0,0],[8.32415887,0.131889924,1.378240479,0.445075077,0,0,0.400301781,0.644875913,0,2.090312059,0,0.844786398,1.105391867,0,2.556375926,0.373762974,0.047148063,0.118527787,1.012080313,0,0,0.172406022,0.903731016,0.401948664,0,0,0,0.127318242,0],[1.764546512,0,0,0,0,1.214737189,0,0,0,0.625832391,0.35513382,0,0,0,0.271382744,0,0,0,0,0,0,0,0,0,0.738994212,0.92606833,0,0,0],[2.277818979,0,0,0,0,0.205745056,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.803436384,0,0,0,0,0,0,0,0,0.50046683,0,0.205745056,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.829831435,0,0,0,0,0,0,0,0,0.505172443,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0.193563737,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.639183623,0,0,0,0],[0,0,0,0,0,0,0,0,0,0.018102231,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0.443942679,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2.085094556,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1.470095881,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1.853924832,0,1.705056137,0,0.132211401,2.345317957,2.591456902,0,1.062945016,3.791312558,0,0,1.331489923,0,1.187072361,3.294330711,0,0,0,0,0,3.013652306,0.226916313,0,1.145963485,0,0,0,0],[2.904337099,0,0,0,0,0,0,0,0,0.371189344,0,0,0,0,0.165877867,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    #MLR Model
    db = mongo.db.APT_GEO_Context_2021_missing
    docs = db.find()

    df = pd.DataFrame(list(docs))

    #Spliting inputs and output variables
    inputs = df.iloc[:, [7,9,13,14,18,19,23,24,28,29,33,34]]
    output = df.iloc[:, [8]]

    regr = linear_model.LinearRegression()
    regr.fit(inputs, output)

    #Prediction
    #Retrieve existing data
    first_year = int(year) - 5

    if int(year) > (last_collection_year + 1):
        #Some data out of bounds
        result["prediction"] = 0
        result["prediction_error"] = "None"
        result["real_incidents"] = "None"
        result["deviation"] = 0
        #Chart
        chartOptions = {}

        #Series
        serie = {}
        serie['name'] = "Real_Incidents"
        serie_data = []
        serie_data.append(0)
        serie_data.append(0)
        serie_data.append(0)
        serie_data.append(0)
        serie_data.append(0)
        serie_data.append(0)
        serie['data'] = serie_data

        chartOptions['series'] = [serie]

        #Options
        options = {}
        options['color'] = ['#6ab04c', '#2980b9']
        options['chart'] = {'background': 'transparent'}
        options['dataLabels'] = {'enabled': False}
        options['stroke'] = {'curve': 'smooth'}
        options['xaxis'] = {'categories': [str(int(year)-5), str(int(year)-4), str(int(year)-3), str(int(year)-2), str(int(year)-1), str(int(year))]}
        options['legend'] = {'position': 'top'}
        options['grid'] = {'show': False}
        chartOptions['options'] = options

        result['chartOptions'] = chartOptions
        return jsonify(result)

    else:
        #All in bounds
        complete_db = mongo.db.APT_GEO_Context_complete
        
        try:
            #Easy Mode
            complete_docs = complete_db.find({"$and":[ {"country1_code":country1_code}, {"country2_code": country2_code}, {"incident_year":year}]})

            df = pd.DataFrame(list(complete_docs))
            inputs = df.iloc[:, [7,9,13,14,18,19,23,24,28,29,33,34]]
            output = df.iloc[:, [8]]

            real_incidents = [output.iloc[0].values.tolist()][0][0]

            prediction = regr.predict([inputs.iloc[0].values.tolist()])[0][0]

            result["prediction"] = prediction
            
            if int(year) <= 2020:
                result["prediction_error"] = abs(prediction - real_incidents)
            else:
                result["prediction_error"] = "Not yet"


            result["real_incidents"] = real_incidents

            if country2_code == 'ESP' and int(year) == 2021:
                result["real_incidents"] = 12

            #Deviation
            country1_index = attacking_countries.index(country1_code)
            country2_index = affected_countries.index(country2_code)

            result["deviation"] = deviation_matrix[country2_index][country1_index]

            #Chart
            chartOptions = {}

            #Series
            serie = {}
            serie['name'] = "Real_Incidents"
            serie_data = []
            serie_data.append(int(inputs.iloc[0][10]))
            serie_data.append(int(inputs.iloc[0][8]))
            serie_data.append(int(inputs.iloc[0][6]))
            serie_data.append(int(inputs.iloc[0][4]))
            serie_data.append(int(inputs.iloc[0][2]))
            serie_data.append(int([output.iloc[0].values.tolist()][0][0]))
            serie['data'] = serie_data

            chartOptions['series'] = [serie]

            #Options
            options = {}
            options['color'] = ['#6ab04c', '#2980b9']
            options['chart'] = {'background': 'transparent'}
            options['dataLabels'] = {'enabled': False}
            options['stroke'] = {'curve': 'smooth'}
            options['xaxis'] = {'categories': [str(int(year)-5), str(int(year)-4), str(int(year)-3), str(int(year)-2), str(int(year)-1), str(int(year))]}
            options['legend'] = {'position': 'top'}
            options['grid'] = {'show': False}
            chartOptions['options'] = options
 
            result['chartOptions'] = chartOptions

            return jsonify(result)

        except:
            #Hard Mode
            
            #Check Number of incidents bwtween country pair
            contry_pair_db = mongo.db.APT_Total_incidents_by_country_pairs
            stats_doc = contry_pair_db.find_one()

            input_list = []

            input_list.append(stats_doc[country1_code+'_'+country2_code])

            for target_year_dif in range(0, 6):

                target_year = (int(year) - target_year_dif)
                
                completed = False

                complete_docs = complete_db.find({"$and":[ {"country1_code":country1_code}, {"country2_code": country2_code}]})

                for doc in complete_docs:

                    if not completed:

                        if (target_year < int(doc['incident_year']) and target_year >= (int(doc['incident_year'])-5)):
                            for match_year in range(0, 6):
                                if (int(doc['incident_year']) - match_year) == target_year:
                                    completed = True
                                    #Append Number of Incidents
                                    if target_year == int(year):
                                        real_incidents = int(doc['incidents_'+str(match_year)])
                                        result["real_incidents"] = real_incidents
                                    else:
                                        input_list.append(doc['incidents_'+str(match_year)])
                                    #Append Godlstein Index percentaje
                                    input_list.append(doc['positive_goldstein_mentions_'+str(match_year)])
                                    

                if not completed:
                    result["prediction"] = 0
                    result["prediction_error"] = "None"
                    result["real_incidents"] = "None"
                    result["deviation"] = 0
                    #Chart
                    chartOptions = {}

                    #Series
                    serie = {}
                    serie['name'] = "Real_Incidents"
                    serie_data = []
                    serie_data.append(0)
                    serie_data.append(0)
                    serie_data.append(0)
                    serie_data.append(0)
                    serie_data.append(0)
                    serie_data.append(0)
                    serie['data'] = serie_data

                    chartOptions['series'] = [serie]

                    #Options
                    options = {}
                    options['color'] = ['#6ab04c', '#2980b9']
                    options['chart'] = {'background': 'transparent'}
                    options['dataLabels'] = {'enabled': False}
                    options['stroke'] = {'curve': 'smooth'}
                    options['xaxis'] = {'categories': [str(int(year)-5), str(int(year)-4), str(int(year)-3), str(int(year)-2), str(int(year)-1), str(int(year))]}
                    options['legend'] = {'position': 'top'}
                    options['grid'] = {'show': False}
                    chartOptions['options'] = options
        
                    result['chartOptions'] = chartOptions
                    return jsonify(result)

            #If input list is complete
            prediction = regr.predict([input_list])[0][0]
            result["prediction"] = prediction
            result["prediction_error"] = abs(prediction - real_incidents)
            #Deviation
            country1_index = attacking_countries.index(country1_code)
            country2_index = affected_countries.index(country2_code)
            result["deviation"] = deviation_matrix[country2_index][country1_index]

            #Chart
            chartOptions = {}

            #Series
            serie = {}
            serie['name'] = "Real_Incidents"
            serie_data = []
            serie_data.append(int(input_list[10]))
            serie_data.append(int(input_list[8]))
            serie_data.append(int(input_list[6]))
            serie_data.append(int(input_list[4]))
            serie_data.append(int(input_list[2]))
            serie_data.append(int(real_incidents))
            serie['data'] = serie_data

            chartOptions['series'] = [serie]

            #Options
            options = {}
            options['color'] = ['#6ab04c', '#2980b9']
            options['chart'] = {'background': 'transparent'}
            options['dataLabels'] = {'enabled': False}
            options['stroke'] = {'curve': 'smooth'}
            options['xaxis'] = {'categories': [str(int(year)-5), str(int(year)-4), str(int(year)-3), str(int(year)-2), str(int(year)-1), str(int(year))]}
            options['legend'] = {'position': 'top'}
            options['grid'] = {'show': False}
            chartOptions['options'] = options
 
            result['chartOptions'] = chartOptions
            return jsonify(result)  



if __name__ == "__main__":
    app.run(debug=True)
