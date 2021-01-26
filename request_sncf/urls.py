import json
import csv
import requests
import logging
from pprint import pprint 


def main():

    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
    headers = {"Authorization": "75cad487-3e50-4835-a3b5-299fc791dcd5"}

    def read_json(): # read and saves json

        response = requests.get(url, headers=headers) #pop up for password
        # raw_data = json.loads(response.text) #dict
        with open('url_sncf.json', mode="w") as file:
            json.dump(response.text, file)
# returns nothing, saves json



    def read_links():

        with open('url_sncf.json') as json_stop_areas_file:
            data = json.load(json_stop_areas_file)

        links = data['links'] # 11 dict with 1 href in each

        list_hrefs = []

        for loop_link in links:

            if type(loop_link) == dict:
                if "href" in loop_link.keys():
                    local_href = loop_link["href"]
                    list_hrefs.append(local_href)
                else:
                    print("Missing key id")
            else:
                print(f"Unexpected format {type(loop_link)}") 

        return list_hrefs



    def save_csv(filepath, list): 
        with open(filepath, mode="w", newline='') as f:
            csv_writer = csv.writer(f, delimiter=';')
        if type(data_rows) == list:
            for row in data_rows:
                # écriture du contenu du row dans la nouvelle ligne du fichier csv
                csv_writer.writerow(row)
        else: 
            print("Unexpected input")

    def save_links(): 

        read_json()
        my_list = read_links()
        save_csv('endpoints_sncf.csv', my_list)


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