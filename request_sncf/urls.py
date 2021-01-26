import json
import csv
import requests
import logging
from pprint import pprint 



logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_urls_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init urls_request.py")



r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth = ('75cad487-3e50-4835-a3b5-299fc791dcd5', ''))

if r.status_code == 200:
    print('Success!')
    logging.info("status code 200")
elif r.status_code != 200:
    print('not Found.')
    logging.warning("status code {r.status_code}")   

with open("url_sncf.json", "w") as API:
    json.dump(r.text, API)
    logging.info("json.dump ok")

doc = r.json()
print(type(doc))
pprint(doc)

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


try:
    with open('endpoints_sncf.csv', 'w') as file:
        header = ['URLS']
        csv_writer = csv.writer(file, delimiter='\t') 
        csv_writer.writerow(header)
        logging.info("csv Writer(header) ok")
        csv_writer.writerow(list_href) #acces row [i]
    logging.info("csv Writer ok")

except:
    logging.warning("Erreur fichier endpoints CSV") 