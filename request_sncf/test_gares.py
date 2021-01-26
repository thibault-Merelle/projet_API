import unittest
import os
from gares import Gares

class TestGares(unittest.TestCase):

    def test_json(self):
        c = Gares()
        c.fgares_request()
        self.assertTrue(os.path.isfile('gares_sncf.json'))
        #self.assertTrue(os.path.exists('gares_sncf.json'))

    def test_csv(self):
        c = Gares()
        c.fgares_storage()
        self.assertTrue(os.path.isfile('gares_sncf.csv'))



        

#python3 -m unittest test_calc.py
if __name__ == '__main__':
    unittest.main()