import json
import csv
import requests
import logging
import os




logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_gares_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')  

logging.info("init gares.py")

class MyGares:

    def __init__(self):
        self.pages = 0
        self.URL = 'https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000'
        self.token = ('75cad487-3e50-4835-a3b5-299fc791dcd5', '')
        self.json_file = 'gares_sncf'
        self.csv_file = 'gares_sncf'
        self.list_id = [] #liste des stop_area
        self.list_label = [] #list code nom
        self.list_name = [] #list noms 
        self.list_out = [] #list resultats



    def fgares_request(self):
        r = requests.get(self.URL +"&start_page="+str(self.pages), auth=self.token)
        if r.status_code == 200:
            logging.info("status code 200")
        elif r.status_code != 200:
            logging.warning("status code {r.status_code}") 
        return r  


    def fgares_write(self, r):
        with open(self.json_file + ".json", "w") as API:
            json.dump(r.text, API)
            logging.info("json.dump ok")
            mydoc = r.json()
        #self.pages +=1    
        return mydoc
        #récursion possible : fgares_request(self, pages+1)



    def fgares_finder(self, mydoc):  
        for loop_area in mydoc["stop_areas"]:
            if isinstance(loop_area, dict):
                if "id" in loop_area.keys():
                    self.list_id.append(loop_area['id'])
                    logging.info("id found !")
                if "name" in  loop_area.keys():
                    self.list_name.append(loop_area['name'])  
                    logging.info("name found !")   
                if "label" in  loop_area.keys():
                    self.list_label.append(loop_area['label'])
                    logging.info("label found !")
                
                else:
                    logging.warning("keys not in areas")
            else:
                logging.warning("unexpeted format (dict expected): {type(loop_area)}")        



    def fgares_storage(self):
        self.list_out = zip(self.list_id, self.list_name, self.list_label)

        try:
            with open(self.csv_file + ".csv", 'w') as file:
                header = ['code_area','name', 'Label']
                csv_writer = csv.writer(file, delimiter='\t') 
                csv_writer.writerow(header)
                logging.info("csv Writer(header) ok")
                for line in self.list_out:
                    csv_writer.writerow(line)
            logging.info("csv Writer ok")

        except:
            logging.warning("Erreur fichier gares CSV") 



         