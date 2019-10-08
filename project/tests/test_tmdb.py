# project/tests/test_api.py


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
        # TODO check if all the shows are in the good format

    def test_search(self):
        """ Testing the TMDB API search endpoint """
        response = Tmdb.search('ozark')
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format

    def test_detail(self):
        """ Testing the TMDB API get show """
        response = Tmdb.detail(69740)
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(data['id'])
        self.assertTrue(data['name'])
        # TODO finish checks on other attributes

    def test_similar(self):
        """ Testing the TMDB API similar endpoint """
        response = Tmdb.similar(69740)
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format

if __name__ == '__main__':
    unittest.main()
