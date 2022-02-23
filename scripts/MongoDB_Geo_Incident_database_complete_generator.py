# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')

#Source
collection = db.APT_GEO_Context_raw

collection_docs = collection.find()

collection_complete = db.APT_GEO_Context_complete

incidents_collection = db.APT_Total_incidents_by_country_pairs_years

incidents_doc = incidents_collection.find_one()

dict_list = []

for doc in collection_docs:
    
    doc_dict = {}
    
    insertion_tag = True
    
    for i in range(0, 6):
        
        try:
            if str(doc['positive_goldstein_mentions_'+str(i)]) == 'nan':
                insertion_tag = False
        
        except:
            insertion_tag = False
        
        try:
            if str(doc['negative_goldstein_mentions_'+str(i)]) == 'nan':
                insertion_tag = False
        
        except:
            insertion_tag = False
        
        try:
            if str(doc['golds_mean_'+str(i)]) == 'nan':
               insertion_tag = False
        
        except:
            insertion_tag = False
        
        try:
            if str(doc['golds_std_'+str(i)]) == 'nan':
                insertion_tag = False
        
        except:
            insertion_tag = False
            
    if insertion_tag:
        
        doc_dict['_id'] = doc['_id']
        doc_dict['country1_code'] = doc['country1_code']
        doc_dict['country2_code'] = doc['country2_code']
        doc_dict['incident_id'] = doc['incident_id']
        doc_dict['incident_year'] = doc['incident_year']
        doc_dict['country1_snt_incidents'] = doc['country1_snt_incidents']
        doc_dict['contry2_rvd_incidents'] = doc['contry2_rvd_incidents']
        doc_dict['country1_to_country2_incidents'] = doc['country1_to_country2_incidents']
        
        country_1 = doc['country1_code']
    
        country_2 = doc['country2_code']
        
        year = int(doc['incident_year'])
        
        
        for i in range(0, 6):
            
            current_year = year - i
            
            try:
                year_tag = incidents_doc[str(current_year)+"_"+country_1+"_"+country_2]
            except:
                year_tag = 0
            
            doc_dict['incidents_'+str(i)] = year_tag
            doc_dict['positive_goldstein_mentions_'+str(i)] = doc['positive_goldstein_mentions_'+str(i)]
            doc_dict['negative_goldstein_mentions_'+str(i)] = doc['negative_goldstein_mentions_'+str(i)]
            doc_dict['golds_mean_'+str(i)] = doc['golds_mean_'+str(i)]
            doc_dict['golds_std_'+str(i)] = doc['golds_std_'+str(i)]
          
        dict_list.append(doc_dict)
        
collection_complete.insert_many(dict_list)
            
            
        
