# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

import pandas as pd
import numpy as np
import time
import os
from tqdm import tqdm
#Bigquery
from google.cloud import bigquery

#MongoDB Connection
from pymongo import MongoClient

#Concurrency
import concurrent.futures

#BigQuery Connection
gcp_project = 'tfm-gdelt'
bq_dataset = 'gdelt-bq.full'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= r'C:\Python\TFM\venv\tfm-gdelt-1e1015a9e20b.json'
#Connection
client_bq = bigquery.Client(project=gcp_project)
dataset_ref = client_bq.dataset(bq_dataset)

#MongoDB Connection
client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')

#First Dataset Reading
incident_set = db.APT_Group_Incidents_CAMEO
incident_docs = incident_set.find()

#Incidents sent by country dataset Reading
incidents_sent_by_country = db.APT_Incident_count_sent_by_country
incidents_sent_country = incidents_sent_by_country.find_one()

#Incidents received by country dataset Reading
incidents_received_by_country = db.APT_Incident_count_received_by_country
incidents_received_country = incidents_received_by_country.find_one()

#Incidents by country pairs dataset Reading
incident_count_by_country_pairs = db.APT_Incident_count_by_country_pairs
incident_count_country_pairs = incident_count_by_country_pairs.find_one()

#Second dataset
geo_set = db.APT_GEO_Context


#GDELT Events Columns Schema
"""

Full fields description: http://data.gdeltproject.org/documentation/GDELT-Event_Codebook-V2.0.pdf

0. GlobalEventID. (integer) 

1. Day. (integer)

2. MonthYear. (integer) 

3. Year. (integer) 

4. FractionDate. (floating point)

5. Actor1Code. (string) 

6. Actor1Name. (string)

7. Actor1CountryCode. (string)

8. Actor1KnownGroupCode. (string)

9. Actor1EthnicCode. (string)

10. Actor1Religion1Code. (string)

11. Actor1Religion2Code. (string) 

12. Actor1Type1Code. (string) 

13. Actor1Type2Code. (string)

14. Actor1Type3Code. (string) 

15. Actor2Code. (string) 

16. Actor2Name. (string)

17. Actor2CountryCode. (string)

18. Actor2KnownGroupCode. (string)

19. Actor2EthnicCode. (string)

20. Actor2Religion1Code. (string)

21. Actor2Religion2Code. (string) 

22. Actor2Type1Code. (string) 

23. Actor2Type2Code. (string)

24. Actor2Type3Code. (string)

25. IsRootEvent. (integer) 

26. EventCode. (string) 

27. EventBaseCode. (string) 

28. EventRootCode. (string) 

29. QuadClass. (integer) 

30. GoldsteinScale. (floating point) 

31. NumMentions. (integer) 

32. NumSources. (integer)

33. NumArticles. (integer) 

34. AvgTone. (numeric) 

35. Actor1Geo_Type. (integer)

36. Actor1Geo_Fullname. (string)

37. Actor1Geo_CountryCode. (string)

38. Actor1Geo_ADM1Code. (string)

39. Actor1Geo_ADM2Code. (string)

40. Actor1Geo_Lat. (floating point) 

41. Actor1Geo_Long. (floating point) 

42. Actor1Geo_FeatureID. (string)

43. Actor2Geo_Type. (integer)

44. Actor2Geo_Fullname. (string)

45. Actor2Geo_CountryCode. (string)

46. Actor2Geo_ADM1Code. (string)

47. Actor2Geo_ADM2Code. (string)

48. Actor2Geo_Lat. (floating point) 

49. Actor2Geo_Long. (floating point) 

50. Actor2Geo_FeatureID. (string)

51. Actor2Geo_Type. (integer)

52. Actor2Geo_Fullname. (string)

53. Actor2Geo_CountryCode. (string)

54. Actor2Geo_ADM1Code. (string)

55. Actor2Geo_ADM2Code. (string)

56. Actor2Geo_Lat. (floating point) 

57. Actor2Geo_Long. (floating point) 

58. Actor2Geo_FeatureID. (string)

59. DATEADDED. (integer) 

60. SOURCEURL. (string)

"""


#Second DataSet Format:
"""

1. CAMEO Country code of the country responsible for the incident

2. CAMEO Country code of the country affected by the incident

3. Incident ID

4. Incident year

5. Total Number of incidents perpetrated by the first country

6. Total Number of incidents received by the second country

7. Number of incidents from the first country to the second country

8. Number of events between the first and second country with a positive Goldstein index during the fifth year prior to the incident

9. Number of events between the first and second country with negative Goldstein index during the fifth year prior to the incident

10. Goldstein mean of events between the first and second country during the fifth year prior to the incident

11. Goldstein Standard deviation of events between the first and second country during the fifth year prior to the incident

12. Number of events between the first and second country with a positive Goldstein index during the fourth year prior to the incident

13. Number of events between the first and second country with negative Goldstein index during the fourth year prior to the incident

14. Goldstein mean of events between the first and second country during the fourth year prior to the incident

15. Goldstein Standard deviation of events between the first and second country during the fourth year prior to the incident

16. Number of events between the first and second country with a positive Goldstein index during the third year prior to the incident

17. Number of events between the first and second country with negative Goldstein index during the third year prior to the incident

18. Goldstein mean of events between the first and second country during the third year prior to the incident

19. Goldstein Standard deviation of events between the first and second country during the third year prior to the incident

20. Number of events between the first and second country with a positive Goldstein index during the second year prior to the incident

21. Number of events between the first and second country with negative Goldstein index during the second year prior to the incident

22. Goldstein mean of events between the first and second country during the second year prior to the incident

23. Goldstein Standard deviation of events between the first and second country during the second year prior to the incident

24. Number of events between the first and second country with a positive Goldstein index during the first year prior to the incident

25. Number of events between the first and second country with negative Goldstein index during the first year prior to the incident

26. Goldstein mean of events between the first and second country during the first year prior to the incident

27. Goldstein Standard deviation of events between the first and second country during the first year prior to the incident

28. Number of events between the first and second country with a positive Goldstein index during the incident year 

29. Number of events between the first and second country with negative Goldstein index during the incident year 

30. Goldstein mean of events between the first and second country during the incident year 

31. Goldstein Standard deviation of events between the first and second country during the incident year

""" 
     
def gcp2df(sql):
    query = client_bq.query(sql)
    results = query.result()
    return results.to_dataframe()
  
"""
def geo_data(doc):
    
    if len(doc["cameo_operation_countries"]) < 30:
        
        start = time.time()
    
        first_country_cameo = doc["cameo_country"]
        op_year = doc["operation_year"]
        op_id = doc["_id"]
        #5.
        first_country_incidents_sent = incidents_sent_country[first_country_cameo]
            
        #Iterate over the affected countries
        with tqdm(total = len(doc["cameo_operation_countries"])) as pbar:
            for second_country_cameo in doc["cameo_operation_countries"]:
                
                #6.
                second_country_incidents_received = incidents_received_country[second_country_cameo]
                #7.
                first_country_to_second_country_incidents = incident_count_country_pairs[first_country_cameo+"_"+second_country_cameo]
                
                #Iterate over GDELT files from fifth year prior to the incident to the incident year
                bound_year = int(op_year) - 5
                
                dataset_row = {}
                
                #Append 1.
                dataset_row["country1_code"] = first_country_cameo
                #Append 2.
                dataset_row["country2_code"] = second_country_cameo
                #Append 3.
                dataset_row["incident_id"] = op_id
                #Append 4.
                dataset_row["incident_year"] = op_year
                #Append 5.
                dataset_row["country1_snt_incidents"] = first_country_incidents_sent
                #Append 6.
                dataset_row["contry2_rvd_incidents"] = second_country_incidents_received
                #Append 7.
                dataset_row["country1_to_country2_incidents"] = first_country_to_second_country_incidents
                
                for year in range(bound_year, int(op_year)+1):
    
                    pos_golds_numb = 0
                    neg_golds_numb = 0
                    year_means = []
                    year_stds = []
                    bound_counter = 0
                    
                    if year < 2015:
                        
                        #GDELT 1.0
                        for gdelt_file in os.listdir(r'C:\Python\TFM\venv\Gdelt_1.0_Events_Database/'+str(year)+'/'):
                                
                            #Importing gdelt file into pandas dataframe
                            gdelt_data = pd.read_csv(r'C:\Python\TFM\venv\Gdelt_1.0_Events_Database/'+str(year)+'/'+gdelt_file, header=None,  delimiter='	', usecols=[7, 17, 34])
                            
                            gdelt_data = gdelt_data[(gdelt_data[7] == first_country_cameo) & (gdelt_data[17] == second_country_cameo)]
                            
                            
                            if len(gdelt_data) == 0:
                                bound_counter += 1
                                
                            if bound_counter > 10:
                                break
                                
                            if len(gdelt_data) > 0:   
                                #Number of positive goldstein indexes
                                pos_golds = len(gdelt_data[(gdelt_data[34] >= 0)])
                                
                                #Add number of positive goldstein indexes
                                pos_golds_numb += pos_golds
                                
                                #Ass number of negative goldstein indexes
                                neg_golds_numb += (len(gdelt_data) - pos_golds)
                                
                                
                                #Calular media Goldstein
                                #Append to list
                                year_means.append(np.mean(gdelt_data[34].to_numpy(), dtype=np.float64))
                            
                                #Calcular desviación típica
                                #Append to dict
                                year_stds.append(np.std(gdelt_data[34].to_numpy(), dtype=np.float64))
                                
                    else:
                        
                        #GDELT 2.0
                        gdelt_data = gcp2df("SELECT GoldsteinScale FROM `gdelt-bq.full.events` WHERE Actor1Code LIKE '"+first_country_cameo+"' AND Actor2Code LIKE '"+second_country_cameo+"' AND Year LIKE '"+str(year)+"' LIMIT 5000")
                        
                        for gdelt_file in os.listdir(r'E:\Gdelt_2.0_Events_Database/'+str(year)+'/'):
                            
                            if np.random.random(1) > 0.998 :
                                
                                #Importing gdelt file into pandas dataframe
                                gdelt_data = pd.read_csv(r'E:\Gdelt_2.0_Events_Database/'+str(year)+'/'+gdelt_file, header=None,  delimiter='	', usecols=[7, 17, 34])
                                
                                gdelt_data = gdelt_data[(gdelt_data[7] == first_country_cameo) & (gdelt_data[17] == second_country_cameo)]
                                
                                
                                if len(gdelt_data) == 0:
                                    bound_counter += 1
                                    
                                if bound_counter > 100:
                                    break
                                    
                                if len(gdelt_data) > 0:   
                                    #Number of positive goldstein indexes
                                    pos_golds = len(gdelt_data[(gdelt_data[34] >= 0)])
                                    
                                    #Add number of positive goldstein indexes
                                    pos_golds_numb += pos_golds
                                    
                                    #Ass number of negative goldstein indexes
                                    neg_golds_numb += (len(gdelt_data) - pos_golds)
                                    
                                    
                                    #Calular media Goldstein
                                    #Append to list
                                    year_means.append(np.mean(gdelt_data[34].to_numpy(), dtype=np.float64))
                                
                                    #Calcular desviación típica
                                    #Append to dict
                                    year_stds.append(np.std(gdelt_data[34].to_numpy(), dtype=np.float64))
                        
                        
                    try:
                        tag = str(int(op_year)-year)
                        dataset_row["positive_goldstein_mentions_"+tag] = pos_golds_numb
                        dataset_row["negative_goldstein_mentions_"+tag] = neg_golds_numb
                        
                        
                        
                        #List to numpy
                        numpy_year_means = np.array(year_means)
                        numpy_year_stds = np.array(year_stds)
                        
                        
                        dataset_row["golds_mean_"+tag] = np.mean(numpy_year_means, dtype=np.float64)
                        dataset_row["golds_std_"+tag] = np.mean(numpy_year_stds, dtype=np.float64)
                        
                        
                    except Exception as e:
                        print(e)
            
                pbar.update(1)
            geo_set.insert_one(dataset_row)
            
        return time.time() - start
"""       

#Iterating throug Incidents
#with concurrent.futures.ThreadPoolExecutor() as executor:
#    execution_times = [executor.submit(geo_data, doc) for doc in incident_docs]
 
df = gcp2df("SELECT Actor1Code, Actor2Code, Year, GoldsteinScale FROM `gdelt-bq.full.events` WHERE Actor1Code LIKE 'USA' AND Actor2Code LIKE 'RUS' AND Year = 2014 LIMIT 10")
print (df)
