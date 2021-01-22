#!/usr/bin/env python3
import json
import csv
import requests
import logging
from pprint import pprint 

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_Second_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init second_request.py")

depart = stop_area:OCE:SA:87686006
arrivee = stop_area:OCE:SA:87722025
#request api.sncf endpoint = stop_areas
r = requests.get('https://api.sncf.com/v1/coverage/sncf/journeys?from={depart}&to={arrivee}', auth = ('75cad487-3e50-4835-a3b5-299fc791dcd5', ''))
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
#print(doc['links'])
print(len(doc['links']))

areas = doc["stop_areas"]
print(type(areas))
area = areas[0]
list_id = []
list_label = []
list_name = []
list_timezone=[]
for loop_area in areas:
    if type(loop_area) == dict:
        if "id" in loop_area.keys():
            list_id.append(loop_area['id'])
            logging.info("id found !")
        if "label" in  loop_area.keys():
            list_label.append(loop_area['label'])
            logging.info("label found !")
        if "name" in  loop_area.keys():
            list_name.append(loop_area['name'])  
            logging.info("name found !")  
        if "timezone" in  loop_area.keys():
            list_timezone.append(loop_area['timezone'])  
            logging.info("timezone found !")   
        else:
            logging.warning("id key not in areas")
    else:
        logging.warning("unexpeted format (dict expected): {type(loop_area)}")        

print(list_name)
print(list_id)
print(list_label)
print(list_timezone)

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
 
  
#formater les listes en une pour CSV
print(len(list_id))
print(len(list_label))
print(len(list_name))
print(len(list_timezone))
result_init = zip(list_name, list_id, list_label, list_timezone)
result = set(result_init)
print(result)



#fichier csv:

try:
    #avec writer :
    with open('gares_sncf.csv', 'w') as file:
        header = ['Names', 'Areas', 'Label', 'timezone']
        csv_writer = csv.writer(file, delimiter='\t') 
        csv_writer.writerow(header)
        logging.info("csv Writer(header) ok")

        for item in result:
            csv_writer.writerow(item) #acces row [i]
    logging.info("csv Writer ok")

except:
    logging.warning("Erreur fichier Data CSV") 