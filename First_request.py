#!/usr/bin/env python3
import json
import requests
import logging
from pprint import pprint 

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_First_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init First_request.py")

#request api.sncf endpoint = stop_areas
r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth = ('75cad487-3e50-4835-a3b5-299fc791dcd5', ''))

if r.status_code == 200:
    print('Success!')
    logging.info("status code 200")
elif r.status_code == 404:
    print('not Found.')
    logging.warning("status code 404")   

with open("api_sncf.json", "w") as API:
    json.dump(r.text, API)
    logging.info("json.dump ok")

pprint(r.json())




    

#myJson = r.json()
#myJson_formatted = json.dump(myJson, indent=4)

