# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

#Scrapping
from bs4 import BeautifulSoup
import requests

#Others
from time import time
from tqdm import tqdm
from zipfile import ZipFile
import json
import os

#Change working directory to the External Drive
path = "D:\Gdelt_1.0_Events_Database"
os.chdir(path)

gdelt_masterfile = 'http://data.gdeltproject.org/events/index.html'

gdelt_flag = True

#Request
try:    
    gdelt_text = requests.get(gdelt_masterfile, timeout=10)
except:
    print("GDELT 1.0 master file unreached")
    gdelt_flag = False
    
    
#Soup    
try:
    gdelt_soup = BeautifulSoup(gdelt_text.content, 'html.parser')
except:
    print("Unable to soup GDELT 1.0 master file Website")
    gdelt_flag = False

#Master file Scrapping
if gdelt_flag:
    
    #Calculate the number of files to download
    total_progress = 0
    for gdelt_rows in gdelt_soup.find_all("a"):
        if gdelt_rows.get("href")[0] == '1' or gdelt_rows.get("href")[0] == '2':
            total_progress += 1
    
    with tqdm(total = total_progress) as pbar:
        for gdelt_rows in gdelt_soup.find_all("a"):
            url = gdelt_rows.get("href")
            
            if url[0] == '1' or url[0] == '2':
                
                try: 
                                        
                    #Download file
                    with requests.get("http://data.gdeltproject.org/events/"+url) as partial_file:
                        print(partial_file.status_code)
                        with open(url, 'wb') as pfd:
                            pfd.write(partial_file.content)
                    
                    #Decompress file
                    with ZipFile(url) as zip_file:
                        zip_file.extractall("gdelt_database_files")
                        
                    #Remove zipfile
                    os.remove(url)
                    #Updating Status File
                    with open("D:\Gdelt_1.0_Events_Database\gdelt_database_status.json", 'w') as sfd:
                        status_dict = {
                            "source": "http://data.gdeltproject.org/events/index.html",
                            "database": "gdelt 1.0 events",
                            "last_update": url,
                            }
                        json.dump(status_dict, sfd)
                    
                    pbar.update(1)
                    
                    
                except Exception as e:
                    print(e)
                    pbar.update(1)
                    #Include url in failed file
                    with open("failed_files.txt", "a") as ffd:
                        ffd.write(url+'\n')