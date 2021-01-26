import json
import csv
import requests
import logging
import datetime
from gares import Gares

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_routes_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init routes.py")
'''
def get_json(data, i=0):
    i += 1
    if type(data) == dict:
        for key, value in dict(data).items():
            print("    "*(i-1)+"|--->", key, 'dict')
            get_json(value,i)
    elif type(data) == list:
        print("list")
        if len(list(data)) > 0:
            get_json(list(data)[0],i)
'''
class MyRoute:

    def __init__(self):
        self.depart = 'stop_area:OCE:SA:87686006'
        self.arrivee = 'stop_area:OCE:SA:87722025'
        self.URL = 'https://api.sncf.com/v1/coverage/sncf/journeys?'
        self.token = ('75cad487-3e50-4835-a3b5-299fc791dcd5', '')
        self.json_file = "routes_sncf.json"
        self.csv_file = 'routes_sncf.csv'
        self.list_arrivee = []
        self.list_depart = []
        self.list_duration = []
        self.stops = 0

    def froutes_request(self):
        r = requests.get(self.URL + "from=" + self.depart + "&to=" + self.arrivee, auth=self.token)
        if r.status_code == 200:
            print('Success!')
            logging.info("status code 200")
        elif r.status_code != 200:
            print('not Found.')
            logging.warning("status code {r.status_code}")   

        with open(self.json_file, "w") as API:
            json.dump(r.text, API)
            logging.info("json.dump ok")
            mydoc = r.json()
        return mydoc


    def froutes_finder(self, mydoc):

        for loop_journeys in mydoc["journeys"]:
            if type(loop_journeys) == dict:
                if "arrival_date_time" in loop_journeys.keys():
                    self.list_arrivee.append(loop_journeys['arrival_date_time'])
                    logging.info("arrival_date_time found !")
                if "departure_date_time" in  loop_journeys.keys():
                    self.list_depart.append(loop_journeys['departure_date_time'])  
                    logging.info("departure_date_time found !")   
                if "duration" in  loop_journeys.keys():
                    self.list_label.append(loop_journeys['duration'])
                    logging.info("duration found !")
                if "section" in  loop_journeys.keys():
                    [self.stops = len(mydoc["journeys"][0]['section']) if len(mydoc["journeys"][0]['section']) > 2]
                    logging.info("stops found !")
                
                else:
                    logging.warning("keys not in journeys")
            else:
                logging.warning("unexpeted format (dict expected): {type(loop_journeys)}")           




# next_departure = 20210125T151500
#    next_departure_date_format=datetime.datetime.strptime(next_departure, "%Y%m%dT%H%M%S")
#    print(next_departure_arrival_date_format)

#base_arrival = raw_data["journeys"][0]["sections"][1]["stop_date_times"]["base_arrival_date_time"]
#base_arrival_date_format=datetime.datetime.strptime(base_arrival, "%Y%m%dT%H%M%S")

#base_departure = raw_data["journeys"][0]["sections"][1]["stop_date_times"]["base_departure_date_time"]
#base_departure_date_format=datetime.datetime.strptime(base_departure, "%Y%m%dT%H%M%S")
    
#temps_arret = base_departure_date_format - base_arrival_date_format
#print("temps d'arret: ",temps_arret)




    def froutes_storage(self):
        self.list_out = zip(self.list_id, self.list_name, self.list_label)
        self.list_out = set(self.list_out)
        try:
            with open(self.csv_file, 'w') as file:
                header = ['H.départ','H.arrivée', 'T.trajet', 'nb.arrets']
                csv_writer = csv.writer(file, delimiter='\t') 
                csv_writer.writerow(header)
                logging.info("csv Writer(header) ok")
                csv_writer.writerow(self.list_out)
            logging.info("csv Writer ok")

        except:
            logging.warning("Erreur fichier gares CSV") 

c = myroute()

get_json(c.froutes_request(),0)
#c.froutes_storage()     