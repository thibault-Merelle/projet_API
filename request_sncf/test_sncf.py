import unittest
import os
from endpoints import MyEndpoints
from gares import MyGares
from routes import MyRoutes


class TestGares(unittest.TestCase):


            ###### test endpoints.py ########

    def test_json_endpoints(self):
        myclass = MyEndpoints()
        myclass.fep_request()
        self.assertTrue(os.path.isfile(myclass.json_file + '.json'))


    def test_finder_endpoints(self):
        myclass = MyEndpoints()
        myclass.fep_finder(myclass.fep_write(myclass.fep_request()))

        self.assertIsInstance(myclass.list_hrefs, list)
        self.assertTrue(len(myclass.list_hrefs)>0)

        self.assertIsInstance(myclass.list_count, list)
        self.assertTrue(len(myclass.list_count)>0)
           

    def test_csv_routes(self):
        myclass = MyEndpoints()
        myclass.fep_storage()   
        self.assertTrue(os.path.isfile(myclass.csv_file + '.csv'))



            ###### test gares.py ########

    def test_json_gares(self):
        myclass = MyGares()
        myclass.fgares_request()
        self.assertTrue(os.path.isfile(myclass.json_file + '.json'))
        #self.assertTrue(os.path.exists('gares_sncf.json'))


    def test_finder_gares(self):
        myclass = MyGares()
        myclass.fgares_finder(myclass.fgares_request())

        self.assertIsInstance(myclass.list_id, list)
        self.assertTrue(len(myclass.list_id)>0)

        self.assertIsInstance(myclass.list_name, list)
        self.assertTrue(len(myclass.list_name)>0)

        self.assertIsInstance(myclass.list_label, list)
        self.assertTrue(len(myclass.list_label)>0)     


    def test_csv_gares(self):
        myclass = MyGares()
        myclass.fgares_storage()
        self.assertTrue(os.path.isfile(myclass.csv_file + '.csv'))





            ###### test routes.py ########

    def test_json_routes(self):
        myclass = MyRoutes()
        myclass.froutes_request()
        self.assertTrue(os.path.isfile(myclass.json_file + '.json'))


    def test_finder_routes(self):
        myclass = MyRoutes()
        myclass.froutes_finder(myclass.froutes_write(myclass.froutes_request()))

        self.assertIsInstance(myclass.list_stations, list)
        self.assertTrue(len(myclass.list_stations)>0)

        self.assertIsInstance(myclass.list_depart, list)
        self.assertTrue(len(myclass.list_depart)>0)

        self.assertIsInstance(myclass.list_arrivee, list)
        self.assertTrue(len(myclass.list_arrivee)>0)     

        self.assertIsInstance(myclass.list_stops, list)
        self.assertTrue(len(myclass.list_stops)>0)     

        self.assertIsInstance(myclass.list_duration, list)
        self.assertTrue(len(myclass.list_duration)>0)             

    def test_csv_routes(self):
        myclass = MyRoutes()
        myclass.froutes_storage()
        self.assertTrue(os.path.isfile(myclass.csv_file + '.csv'))





#python3 -m unittest test_calc.py
if __name__ == '__main__':
    unittest.main()