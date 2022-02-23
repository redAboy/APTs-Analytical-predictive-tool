# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Miguel Peidro Paredes
"""

import json

#Cameo country codes loading
with open ("cameo_country_codes.json", "r") as fd_out:
    cameo_country_codes = json.load(fd_out)


#Iso country lat and longs loading
with open ("countrycode-latlong.json", "r") as fd_out:
    iso_country_codes_latlong = json.load(fd_out)


#Iso 3166 country codes
with open ("iso_3166_country_codes.json", "r") as fd_out:
    iso_country_codes = json.load(fd_out)



#Generating CAMEO to ISO 3166 country codes
cameo_iso = {}

for iso_country in iso_country_codes:
    
    for cameo_country in cameo_country_codes:
        if iso_country["name"] == cameo_country:
            
            cameo_iso[cameo_country_codes[cameo_country]] = iso_country["alpha2"]
            
            
with open("cameo_to_iso3166.json", 'w') as fd:
    fd.write(json.dumps(cameo_iso))



    