import unittest
import os
from gares import MyGares
from routes import MyRoutes

class TestGares(unittest.TestCase):

    def test_json_gares(self):
        myclass = MyGares()
        myclass.fgares_request()
        self.assertTrue(os.path.isfile('gares_sncf.json'))
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
        self.assertTrue(os.path.isfile('gares_sncf.csv'))

        #self.assertIsInstance(myclass.list_out, list)
        self.assertNotEqual(len(myclass.list_out), 0)



class TestRoutes(unittest.TestCase):

    def test_json_routes(self):
        myclass = MyRoutes()
        myclass.froutes_request()
        self.assertTrue(os.path.isfile('routes_sncf.json'))


    def test_finder_routes(self):
        myclass = MyRoutes()
        myclass.froutes_finder(myclass.froutes_read(myclass.froutes_request()))

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

        #self.assertIsInstance(myclass.list_out, list)
        self.assertTrue(len(myclass.list_out)>0)     

        self.assertTrue(os.path.isfile('routes_sncf.csv'))





#python3 -m unittest test_calc.py
if __name__ == '__main__':
    unittest.main()