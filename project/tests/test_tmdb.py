# project/tests/test_tmdb.py


import unittest
import json

from project.server import db
from project.server.models import Tmdb
from project.tests.base import BaseTestCase


class TestTmdb(BaseTestCase):
    """
    Testing if we have the good responses from the api
    """
    def test_discover(self):
        """ Testing the TMDB API discover endpoint """
        response = Tmdb.discover()
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format (can be from_dict/to_dict)

    def test_search(self):
        """ Testing the TMDB API search endpoint """
        response = Tmdb.search('ozark')
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format (can be from_dict/to_dict)

    def test_detail(self):
        """ Testing the TMDB API get show """
        response = Tmdb.detail(69740)
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(data['id'])
        self.assertTrue(data['name'])
        # TODO check if all the shows are in the good format (can be from_dict/to_dict)

    def test_similar(self):
        """ Testing the TMDB API similar endpoint """
        response = Tmdb.similar(69740)
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format (can be from_dict/to_dict)
    
    def test_seasons(self):
        """ Testing the TMDB API seasons endpoint """
        response = Tmdb.season(tmdb_show_id = 69740, season_number = 1)
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['episodes'], list))
        # TODO check if all the shows are in the good format (can be from_dict/to_dict)
        

if __name__ == '__main__':
    unittest.main()
