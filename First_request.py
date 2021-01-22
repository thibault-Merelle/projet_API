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
#data = json.loads(r.text)

if r.status_code == 200:
    print('Success!')
    logging.info("status code 200")
elif r.status_code != 200:
    print('not Found.')
    logging.warning("status code {r.status_code}")   

with open("api_sncf.json", "w") as API:
    json.dump(r.text, API)
    logging.info("json.dump ok")

doc = r.json()
print(type(doc))
#pprint(doc)

#recherche dans le Json:
  
#recherche dans stop_areas  
[print(key) for key in doc]
print(doc['links'])
print(len(doc['links']))

areas = doc["stop_areas"]
print(type(areas))
area = areas[0]
list_id = []
for loop_area in areas:
    if type(loop_area) == dict:
        if "id" in loop_area.keys():
            list_id.append(loop_area['id'])
        else:
            logging.warning("id key not in areas")
    else:
        logging.warning("unexpeted format (dict expected): {type(loop_area)}")        

print(len(list_id))
print(list_id)

#recherche dans links
links = doc["links"]
print(type(links))
link = links[0]
list_href = []
for loop_href in links:
    if type(loop_href) == dict:
        if "href" in loop_href.keys():
            list_href.append(loop_href['href'])
        else:
            logging.warning("href key not in links")
    else:
        logging.warning("unexpeted format (dict expected): {type(loop_href)}")        

print(len(list_href))
print(list_href)


#print(type(area), area)

#print(area.keys())

#print(area['id'])
#for i in my_list:
#    for 
#        my_ends.append(my_list[0])
      
    #for Value in doc:  
    #    print(doc['links'][0]['href'])    
 
  



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
        