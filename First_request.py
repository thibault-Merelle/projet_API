#!/usr/bin/env python3
import json
import csv
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
elif r.status_code != 200:
    print('not Found.')
    logging.warning("status code {r.status_code}")   

with open("api_sncf.json", "w") as API:
    json.dump(r.text, API)
    logging.info("json.dump ok")

pprint(r.json())


#fichier csv:

try:
    #reader
    with open('gares_sncf.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file) #delimiter à développer
            logging.info("csv Reader ok")
    #        next(csv_reader)
    #        for line in csv_reader:
    #            print(line)
    #avec writer :
            with open('gares_sncf.csv', 'w') as new_file:
                csv_writer = csv.writer(new_file, delimiter='\t') 
                logging.info("csv Writer ok")

                for line in csv_reader:
                    csv_writer.writerow(line) #acces row [i]

except:
    logging.warning("Erreur fichier Data CSV") 
    
#avec dict.writer
#keys = header => plus simple à lire et partager
'''
with open('gares_sncf.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

    with open ('gares_sncf', 'w') as new_file:
        fieldnames = ['AAAA', 'BBBB', 'CCCCC']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv.writer.writeheader()

            for line in csv_reader:
                #del line['CCCCC'] #delete colomn 'CCCC'
                csv.writer.writerow(line)
 '''
        