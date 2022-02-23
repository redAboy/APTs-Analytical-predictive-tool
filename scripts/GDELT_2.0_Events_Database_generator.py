# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

from tqdm import tqdm
from zipfile import ZipFile
import requests
import json
import os


#Change working directory to the External Drive
path = "D:\Gdelt_2.0_Events_Database"
os.chdir(path)

#Updating GDELT Masterfile
#with requests.get("http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt") as rq:
#    with open ("gdelt_masterfile.txt", 'wb') as fd:
#        fd.write(rq.content)

#Check for previous GDELT database status
try:
    #Previous Status Existing
    with open("D:\Gdelt_2.0_Events_Database\gdelt_database_status.json", 'r') as fd:
        status_dict = json.load(fd)
    
    if status_dict["database"] == "gdelt 2.0 events":
        last_url = status_dict["last_update"]
    
    #Number of iterations
    with open("D:\Gdelt_2.0_Events_Database\gdelt_masterfile.txt", 'r+') as fd:
        #Progress counter
        total_progress = 0
        match_flag = False
        for line in fd.readlines():
            splited_line = line.split(" ")
            url = splited_line[2].replace('\n', "")
            if url == last_url:
                match_flag = True
                
            if match_flag:
                if "export" in line:
                    total_progress += 1
                if "mentions" in line:
                    total_progress += 1
        
    with open("D:\Gdelt_2.0_Events_Database\gdelt_masterfile.txt", 'r+') as fd:
        #Progress counter
        match_flag = False
        with tqdm(total = total_progress) as pbar:
            for line in fd.readlines():
                    splited_line = line.split(" ")
                    url = splited_line[2].replace('\n', "")
                    if url == last_url:
                        match_flag = True
                    
                    if match_flag:
                        
                        if "export" in line:
                            file_path = url.replace("http://data.gdeltproject.org/gdeltv2/", "")
                            date = url.replace("http://data.gdeltproject.org/gdeltv2/", "").replace(".translation.export.CSV.zip", "")
                            
                            try: 
                                
                                #Download file
                                with requests.get(url) as partial_file:
                                    print(partial_file.status_code)
                                    with open(file_path, 'wb') as pfd:
                                        pfd.write(partial_file.content)
                                
                                #Decompress file
                                with ZipFile(file_path) as zip_file:
                                    zip_file.extractall("gdelt_database_files")
                                    
                                #Remove zipfile
                                os.remove(file_path)
                                
                    
                                #Updating Status File
                                with open("D:\Gdelt_2.0_Events_Database\gdelt_database_status.json", 'w') as sfd:
                                    status_dict = {
                                        "source": "http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt",
                                        "database": "gdelt 2.0 events",
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
                                    
                        if "mentions" in line:
                            
                            file_path = url.replace("http://data.gdeltproject.org/gdeltv2/", "")
                            date = url.replace("http://data.gdeltproject.org/gdeltv2/", "").replace(".translation.mentions.CSV.zip", "")
                            
                            try: 
                                
                                #Descargar fichero
                                with requests.get(url) as partial_file:
                                    print(partial_file.status_code)
                                    with open(file_path, 'wb') as pfd:
                                        pfd.write(partial_file.content)
                                
                                #Descomprimir fichero
                                with ZipFile(file_path) as zip_file:
                                    zip_file.extractall("gdelt_database_mentions")
                                    
                                #Remove zipfile
                                os.remove(file_path)
                                
                                #Mergear CSV
                                
                    
                                #Updating Status File
                                with open("D:\Gdelt_2.0_Events_Database\gdelt_database_status.json", 'w') as sfd:
                                    status_dict = {
                                        "source": "http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt",
                                        "database": "gdelt 2.0 events",
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
                            
        
        
except:
    #No Previous Status Existing

    with open("D:\Gdelt_2.0_Events_Database\gdelt_masterfile.txt", 'r+') as fd:
        #Progress counter
        total_progress = 0
        for line in fd.readlines():
            total_progress += 1
            
        total_progress = total_progress - (total_progress/3)*2
            
            
    with open("D:\Gdelt_2.0_Events_Database\gdelt_masterfile.txt", 'r+') as fd:    
        with tqdm(total = total_progress) as pbar:
            for line in fd.readlines():
                """
                if "export" in line:
                    splited_line = line.split(" ")
                    url = splited_line[2].replace('\n', "")
                    file_path = url.replace("http://data.gdeltproject.org/gdeltv2/", "")
                    date = url.replace("http://data.gdeltproject.org/gdeltv2/", "").replace(".translation.export.CSV.zip", "")
                    
                    try: 
                        
                        #Descargar fichero
                        with requests.get(url) as partial_file:
                            print(partial_file.status_code)
                            with open(file_path, 'wb') as pfd:
                                pfd.write(partial_file.content)
                        
                        #Descomprimir fichero
                        with ZipFile(file_path) as zip_file:
                            zip_file.extractall("gdelt_database_files")
                            
                        #Remove zipfile
                        os.remove(file_path)
                        
                        #Mergear CSV
                        
            
                        #Updating Status File
                        with open("D:\Gdelt_2.0_Events_Database\gdelt_database_status.json", 'w') as sfd:
                            status_dict = {
                                "source": "http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt",
                                "database": "gdelt 2.0 events",
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
                """           
                        
                if "mentions" in line:
                    splited_line = line.split(" ")
                    url = splited_line[2].replace('\n', "")
                    file_path = url.replace("http://data.gdeltproject.org/gdeltv2/", "")
                    date = url.replace("http://data.gdeltproject.org/gdeltv2/", "").replace(".translation.mentions.CSV.zip", "")
                    
                    try: 
                        
                        #Descargar fichero
                        with requests.get(url) as partial_file:
                            print(partial_file.status_code)
                            with open(file_path, 'wb') as pfd:
                                pfd.write(partial_file.content)
                        
                        #Descomprimir fichero
                        with ZipFile(file_path) as zip_file:
                            zip_file.extractall("gdelt_database_mentions")
                            
                        #Remove zipfile
                        os.remove(file_path)
                        
                        #Mergear CSV
                        
            
                        #Updating Status File
                        with open("D:\Gdelt_2.0_Events_Database\gdelt_database_status.json", 'w') as sfd:
                            status_dict = {
                                "source": "http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt",
                                "database": "gdelt 2.0 events",
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
                        
                        
                        