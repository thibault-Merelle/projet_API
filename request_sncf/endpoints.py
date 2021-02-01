import json
import csv
import requests
import logging
from pprint import pprint 


class MyEndpoints:

    def __init__(self):
        self.URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": "75cad487-3e50-4835-a3b5-299fc791dcd5"}
        self.json_file = 'endpoints_sncf'
        self.csv_file = 'endpoints_sncf'
        self.list_hrefs = []
        self.list_count = []


    def fep_request(self): #request dans stop areas
        r = requests.get(self.URL, headers=self.headers)
        return r
            

    def fep_write(self, r): #ecriture json
        with open(self.json_file + '.json', 'w') as file:
            json.dump(r.text, file)
            mydoc = r.json()
        return mydoc


    def fep_finder(self, mydoc): #recherches dans la liste adresse mydoc['links]
        section = mydoc['links']
        if isinstance(section, list):
            for i, item in enumerate(mydoc['links']):
                if "href" in item.keys():
                    self.list_hrefs.append(item["href"])
                    self.list_count.append(i)



    def fep_storage(self): #csv header = [n°, endpoints]
        self.list_out = zip(self.list_count, self.list_hrefs)
        with open(self.csv_file + ".csv","w", newline='') as file:
            header = ['n°', 'url_endpoints']
            csv_writer = csv.writer(file, delimiter='\t')
            csv_writer.writerow(header)
            for line in self.list_out:
                csv_writer.writerow(line)


'''
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
    with open('endpoints_sncf.csv', 'w', newline='') as file:
        header = ['URLS']
        csv_writer = csv.writer(file, delimiter='\t') 
        csv_writer.writerow(header)
        logging.info("csv Writer(header) ok")
        csv_writer.writerow(list_href) #acces row [i]
    logging.info("csv Writer ok")

except:
    logging.warning("Erreur fichier endpoints CSV") 
    '''