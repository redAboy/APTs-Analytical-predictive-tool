# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""
#Scrapping
from bs4 import BeautifulSoup
import requests
#MongoAtlas
from pymongo import MongoClient

#Others
from string import digits
from time import time
import json
import re
import pycountry

Mitre_groups = 'https://attack.mitre.org/groups/'
Thai_Cert_groups = 'https://apt.thaicert.or.th/cgi-bin/listgroups.cgi'
mitre_iterative_url= 'https://attack.mitre.org'
thai_iterative_url= 'https://apt.thaicert.or.th'

mitre_flag = True
thai_cert_flag = True

#MongoAtlas Parameters
client = MongoClient("mongodb+srv://admin:mongotfm@cluster0.92w80.mongodb.net/TFM?retryWrites=true&w=majority")
db = client.get_database('TFM')
collection = db.APT_Group_Incidents

#File
fd = open('‪debug.txt', 'a')
fd.truncate(0)

#Variables
groups = []
groups_operations = []
group_name = ''
country = ''
first_observation = ''

#Requests
try:    
    Mitre_text = requests.get(Mitre_groups, timeout=10)
except:
    print("Mitre Website unreached")
    mitre_flag = False
    
try:    
    Thai_Cert_text = requests.get(Thai_Cert_groups, timeout=10)
except:
    print("Thai Cert Website unreached")
    thai_cert_flag = False
    
    
#Soups    
try:
    mitre_soup = BeautifulSoup(Mitre_text.content, 'html.parser')
except:
    print("Unable to soup Mitre Website")
    mitre_flag = False
    
try:
    thai_cert_soup = BeautifulSoup(Thai_Cert_text.content, 'html.parser')
except:
    print("Unable to soup Thai Cert Website")
    thai_cert_flag = False

#Mitre Scrapping
if mitre_flag:
    
    for mitre_rows in mitre_soup.find_all("tr")[1:]:
        
        ###First Stage - Groups webpage scrapping###
        #   +group_name
        #   +country
        #   +first_observation
        #   +group_url
        
        
        col_num = 0
        for mitre_cols in mitre_rows.find_all("td"):
                
            #Group url
            if col_num == 0:
                group_url_td = mitre_cols.find('a', href=True)
                group_url = group_url_td.get("href")
                group_url = mitre_iterative_url + group_url
                print("\n")
                print(group_url)
            
            
            #Group Name
            if col_num == 1:
                group_name = mitre_cols.find('a')
                group_name = group_name.text.replace(" ", "")
                print(group_name)
                
            if col_num == 2:
                associated_groups = str(mitre_cols.text)
                associated_groups = associated_groups.replace(" ", "").replace("\n", "")
                
                if associated_groups == "":
                    associated_groups = "Unknown"
                    
                
                print(associated_groups)
            
            #Group Country    
            if col_num == 3:
                #Searching country form group description
                #Merging a texts
                group_descriptions_td = mitre_cols.find_all("p")
                group_descript = ""
                for group_descriptions in group_descriptions_td:
                    group_descript = group_descript + group_descriptions.text
                
                #Searching Country
                group_country = "Unknown"
                for country_py in pycountry.countries:
                    if country_py.name in group_descript:
                        group_country = str(country_py.name)
                        break
            
                print(group_country)
            
            
            col_num += 1

        ###Second Stage - Group webpage scrapping###
        ###For each operation###
        ### +operation_date
        ### +operation_month (if exist)
        ### +operation_year
        ### +operation_description
        ### +operation_urls
        ### +operation_countries
        
        #Group Page Request
        mitre_group_flag = True
        try:    
            group_page = requests.get(group_url, timeout=10)
        except:
            print("Mitre Group Website unreached")
            mitre_group_flag = False
            
        #Group Soup
        try:
            group_soup = BeautifulSoup(group_page.content, 'html.parser')
        except:
            print("Unable to soup Group Website")
            mitre_group_flag = False
            
        #Group Page Scrapping   
        if mitre_group_flag:
            op_body = group_soup.find("div",  {"class": "jumbotron"})
            op_list = op_body.find_all("li")
            for op_li in op_list:
                
                #Operation Description
                op_descriptions_td = op_li.find_all("a")
                op_description = ""
                for op_descriptions in op_descriptions_td:
                    op_description = op_description + op_descriptions.text
                op_description = op_description.replace(" ", "")
                print(op_description)
                
                #Operation Date
                op_date = str(op_description[op_description.find("(")+1:op_description.find(")")])
                
                op_date_split = op_date.split(',')
                
                if len(op_date_split) > 1:
                    op_year = op_date_split[0]
                    
                    remove_digits = str.maketrans('', '', digits)
                    op_month = op_date_split[1].translate(remove_digits).replace(" ", "")
                    
                elif len(op_date_split) == 1:
                    
                    op_month = "None"
                    op_year = op_date_split[0]
                    
                else:
                    op_month = "None"
                    op_year = "None"
                    
                #Operation urls
                op_urls_td = op_li.find_all("a", href=True)
                op_urls = []
                for op_url_td in op_urls_td:
                    op_url = op_url_td.get("href")
                    op_urls.append(op_url)
                
                    #Operation url request
                    operation_url_flag = True
                    try:    
                        operation_text = requests.get(op_url, timeout=10)
                    except Exception as e:
                        print(e)
                        print("Operation Website unreached")
                        operation_url_flag = False
                     #Operation soup  
                    try:
                        operation_soup = BeautifulSoup(operation_text.content, 'lxml')
                    except Exception as e:
                        print(e)
                        print("Unable to soup Operation Website")
                        operation_url_flag = False
                        
                    #Operation Scrapping
                    if operation_url_flag:
                        op_page_content = operation_soup.text
                        op_countries = []
                        #Contries in operation webpage
                        for country_py in pycountry.countries:
                            if country_py.name in op_page_content:
                                op_countries.append(str(country_py.name))
                                print(country_py.name)
                                
                        print(op_countries)
                
                    #Dictionary Generation
                    try:
                        group_op_json = {}
                        group_op_json = {
                        'group_name': group_name,
                        'group_country': group_country,
                        'reference': group_url,
                        'operation_date': op_date,
                        'operation_month': op_month,
                        'operation_year': op_year,
                        'operation_description': op_description,
                        'operation_urls': op_urls,
                        'operation_countries': op_countries
                        }
                        
                        fd.write(json.dumps(group_op_json))
                        fd.write('\n')
                            
                        groups_operations.append(group_op_json)
                        
                    except Exception as e:
                        print (e)


#Thai Cert Scrapping
if thai_cert_flag:
    thai_table = thai_cert_soup.find("table")
    #for thai_rows in thai_table.find_all('tr')[2:-1]:
    for thai_rows in thai_table.find_all('tr')[2:-1]:
        
        ###First Stage - Groups webpage scrapping###
        #   +group_name
        #   +country
        #   +first_observation
        #   +group_url
        
        #Group Name
        group_bs4 = thai_rows.find('a')
        name = True
        try:
            group_name = str(group_bs4.text)
            
        except:
            group_name = "No name"
            name = False
            
        #Country and first_observation
        count = 0
        for thai_cols in thai_rows.find_all('td'):
            if not thai_cols.get('colspan'):
                if count == 2:
                    try:
                        country = str(thai_cols.text.replace('[', '').replace(']', ''))
                    except:
                        country = "Unknown"
                        
                    if country == '':
                        try:
                            for img in thai_cols.find_all('img'):
                                country = img['alt']
                            
                        except:
                            country = "Unknown"
                            
                    
                if count == 3:
                    
                    try:
                        first_observation = str(thai_cols.text)
                    except:
                        first_observation = "Unknown"
                        
                    if first_observation == '':
                        first_observation = "Unknown"
                        
                    
                count += 1
            else:
                country = "Unknown"
                first_observation = "Unknown"
        
        print('\n')
        print('##Group Info')
        print(group_name)
        print(country) 
        print(first_observation)
        print('\n')
        
        #Group_webpage
        group_url = "None"
        try:
            group_url = thai_iterative_url + str(group_bs4.get('href'))
        except:
            group_url = "None"
            
            
        ###Second Stage - Group webpage scrapping###
        ###For each operation###
        ### +operation_date
        ### +operation_month (if exist)
        ### +operation_year
        ### +operation_description
        ### +operation_urls
        ### +operation_countries
        
        #Group Page Request
        thai_cert_group_flag = True
        try:    
            group_page = requests.get(group_url, timeout=10)
        except:
            print("Thai Cert Group Website unreached")
            thai_cert_group_flag = False
            
        #Group Soup
        try:
            group_soup = BeautifulSoup(group_page.content, 'html.parser')
        except:
            print("Unable to soup Group Website")
            thai_cert_group_flag = False
           
        #Group Page Scrapping   
        if thai_cert_group_flag:
            operations_flag = True
            #Check for operations
            
            try:
            
                operations = group_soup.find_all("td", string="Operations performed")
                print(operations)
                
                if operations:
                    operations_flag = False
                    row_num = 0
                    try:
                        row_num = int(operations[0].get('rowspan'))
                    except Exception as e:
                        print(e)
                        
                    print(row_num)
                    #There is Operations of this group
                    group_table = group_soup.find("table")
                    for group_table_rows in group_table.find_all('tr'):
                        
                        #Last operation
                        if row_num == 0:
                            operations_flag = False
                            break
                        
                        for group_cols in group_table_rows.find_all('td'):
                            #Start Scrapping in Operations performed row
                            if "Operations performed" in group_cols.text:
                                operations_flag = True
                                col_num = 0
                                continue
                            
                            if operations_flag:
                                #Scrapping each operation
                                #Operation Date
                                if col_num == 0:
                                    op_date = group_cols.text
                                    #Split date in to month and year
                                    op_date_split = op_date.split(' ')
                                    if len(op_date_split) > 1:
                                        op_month = op_date_split[0]
                                        op_year = op_date_split[1]
                                        
                                    elif len(op_date_split) == 1:
                                        op_month = "None"
                                        op_year = op_date_split[0]
                                        
                                    else:
                                        op_month = "None"
                                        op_year = "None"
                                    
                                    
                                    print(op_month)
                                    print(op_year)
                                    #Next Column
                                    col_num += 1
                                
                                #Operation Body
                                if col_num == 1:
                                    #Operation description without url
                                    op_description = re.sub(r'\<http.*\>$', '', group_cols.text)
                                    #Operation urls
                                    op_urls = []
                                    op_a = group_cols.find_all('a', href=True)
                                    for op in op_a:
                                        
                                        #Extracting Operation url
                                        op_url = op.get('href')
                                        #Including url in op_urls
                                        op_urls.append(op_url)
                                        
                                        #Operation url request
                                        operation_url_flag = True
                                        try:    
                                            operation_text = requests.get(op_url, timeout=10)
                                        except Exception as e:
                                            print(e)
                                            print("Operation Website unreached")
                                            operation_url_flag = False
                                         #Operation soup  
                                        try:
                                            operation_soup = BeautifulSoup(operation_text.content, 'lxml')
                                        except Exception as e:
                                            print(e)
                                            print("Unable to soup Operation Website")
                                            operation_url_flag = False
                                            
                                        #Operation Scrapping
                                        if operation_url_flag:
                                            op_page_content = operation_soup.text
                                            op_countries = []
                                            #Contries in operation webpage
                                            for country_py in pycountry.countries:
                                                if country_py.name in op_page_content:
                                                    op_countries.append(str(country_py.name))
                                                    print(country_py.name)
                                                    
                                        print(op_countries)
                                                    
                                        #Dictionary Generation
                                        try:
                                            group_op_json = {}
                                            group_op_json = {
                                            'group_name': group_name,
                                            'group_country': country,
                                            'reference': group_url,
                                            'operation_date': op_date,
                                            'operation_month': op_month,
                                            'operation_year': op_year,
                                            'operation_description': op_description,
                                            'operation_urls': op_urls,
                                            'operation_countries': op_countries
                                            }
                                            
                                            fd.write(json.dumps(group_op_json))
                                            fd.write('\n')
                                                
                                            groups_operations.append(group_op_json)
                                            
                                        except Exception as e:
                                            print (e)
                                        
                                                                                    
                                                                            
                        
                        if operations_flag:
                            row_num -= 1
                            col_num = 0
                
                else:
                    print("No operations for this group")
            except Exception as e:
                print(e)
            
        
            
                
        #Json Append
        group_json = {}
        group_json = {
            'group_name': group_name,
            'country': country,
            'first_observation': first_observation,
            'reference': group_url
            }
                
        groups.append(group_json)
    

    #for item in groups:
    #   fd.write(json.dumps(item))
    #   fd.write('\n')
    collection.insert_many(groups_operations)

fd.close