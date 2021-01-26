import json
import csv
import requests
import logging
from datetime import datetime, timedelta
from gares import Gares

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_routes_request.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.info("init routes.py")


class MyRoutes:

    def __init__(self):
        self.date_dep = None
        self.depart = 'stop_area:OCE:SA:87686006'
        self.arrivee = 'stop_area:OCE:SA:87722025'
        self.URL = 'https://api.sncf.com/v1/coverage/sncf/journeys?'
        self.token = ('75cad487-3e50-4835-a3b5-299fc791dcd5', '')
        self.json_file = "routes_sncf.json"
        self.csv_file = 'routes_sncf.csv'
        self.list_stations = []
        self.list_arrivee = []
        self.list_depart = []
        self.list_duration = []
        self.list_stops = []


    def str_convert_time(self, mystr):
        return datetime.strptime(mystr.replace('T',''), '%Y%m%d%H%M%S')
        logging.info("f str_convert_time ok")


    def time_convert_str(self, mytime):
        self.date_dep = datetime.strftime(mytime, '%Y%m%dT%H%M%S')
        logging.info("f time_convert_str ok")


    def froutes_request(self):
        r = requests.get(self.URL + "from=" + self.depart + "&to=" + self.arrivee, auth=self.token)#.json()     + "&datetime=" + self.date_depart
        if r.status_code == 200:
            print('Success!')
            logging.info("status code 200")
        elif r.status_code != 200:
            print('not Found.')
            logging.warning("status code {r.status_code}")   
        return r

    def froutes_read(self, r):

        with open(self.json_file, "w") as API:
            json.dump(r.text, API)
            logging.info("json.dump ok")
            mydoc = r.json()
            return mydoc

    def froutes_finder(self, mydoc):
        section = mydoc['journeys'][0]['sections'][1]

        if isinstance(section, dict) and "stop_date_times" in section :
            for i in section['stop_date_times']:
                self.list_stations.append(i['stop_point']['name'])
                self.list_depart.append(self.str_convert_time(i['departure_date_time']))
                self.list_arrivee.append(self.str_convert_time(i['arrival_date_time']))
                self.list_stops.append(i)

        self.list_duration = [x - y for x, y in zip(self.list_depart, self.list_arrivee)]


    def froutes_storage(self):
        self.list_out = zip(self.list_stops, self.list_stations, self.list_depart, self.list_arrivee, self.list_duration)
        self.list_out = set(self.list_out)
        try:
            with open(self.csv_file, 'w') as file:
                header = ['nb.arrets', 'stations', 'H.départ','H.arrivée', 'T.trajet']
                csv_writer = csv.writer(file, delimiter='\t') 
                csv_writer.writerow(header)
                logging.info("csv Writer(header) ok")
                csv_writer.writerow(self.list_out)
            logging.info("csv Writer ok")

        except:
            logging.warning("Erreur fichier gares CSV") 



'''       
        for n, journey in enumerate(mydoc["journeys"], 1):
            if isinstance(journey, dict) and 'sections' in journey:
                for section in journey['section']:
                    if 'stop_date_times' in section:
                        for stop in section['stop_date_times']:
                            self.list_stops.append(section['stop_date_times']['stop_point']['name'])
                            date_arr = datetime.datetime.strftime(section['stop_date_times']['base_arrival_date_time'], %Y%m%dT%H%M%S")
                            date_dep = datetime.datetime.strftime(section['stop_date_times']['base_departure_date_time'], %Y%m%dT%H%M%S")
                            self.list_arrivee.append(date_arr)
                            self.list_depart.append(date_dep)



        for loop_journeys in mydoc["journeys"]:
            if type(loop_journeys) == dict:
                if "arrival_date_time" in loop_journeys.keys():
                    self.list_arrivee.append(loop_journeys['arrival_date_time'])
                    logging.info("arrival_date_time found !")
                if "departure_date_time" in  loop_journeys.keys():
                    self.list_depart.append(loop_journeys['departure_date_time'])  
                    logging.info("departure_date_time found !")   
                if "duration" in  loop_journeys.keys():
                    self.list_duration.append(loop_journeys['duration'])
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


'''


c = MyRoutes()
c.froutes_finder(c.froutes_read(c.froutes_request()))
c.froutes_storage
#c = MyRoute()
#c.froutes_storage()     