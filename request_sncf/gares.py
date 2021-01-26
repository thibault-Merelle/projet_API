import json
import csv
import requests
import logging




logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_gares_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init gares.py")

class Gares:

    def __init__(self):
        self.pages = 1
        self.URL = 'https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000'
        self.token = ('75cad487-3e50-4835-a3b5-299fc791dcd5', '')
        self.json_file = "gares_sncf.json"
        self.csv_file = 'gares_sncf.csv'
        self.list_id = [] #liste des stop_area
        self.list_label = [] #list code nom
        self.list_name = [] #list noms 
        self.list_out = [] #list resultats



    def fgares_request(self):
        r = requests.get(self.URL +"&start_page="+str(self.pages), auth=self.token)
        if r.status_code == 200:
            print('Success!')
            logging.info("status code 200")
        elif r.status_code != 200:
            print('not Found.')
            logging.warning("status code {r.status_code}")   

        with open(self.json_file, "w") as API:
            json.dump(r.text, API)
            logging.info("json.dump ok")
            doc = r.json()
        self.pages +=1    
        return doc
        #récursion !! fgares_request(self, pages+1)



    def fgare_finder(self, doc):  
        for loop_area in doc["stop_areas"]:
            if type(loop_area) == dict:
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



    def fgare_storage(self):
        self.list_out = zip(self.list_id, self.list_name, self.list_label)
        self.list_out = set(self.list_out)
        try:
            with open(self.csv_file, 'w') as file:
                header = ['code_area','name', 'Label']
                csv_writer = csv.writer(file, delimiter='\t') 
                csv_writer.writerow(header)
                logging.info("csv Writer(header) ok")
                csv_writer.writerow(self.list_out)
            logging.info("csv Writer ok")

        except:
            logging.warning("Erreur fichier gares CSV") 



c = gares()
while c.pages < 5 :
    c.fgare_finder(c.fgares_request())
c.fgare_storage()          