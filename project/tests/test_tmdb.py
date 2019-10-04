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
        response = Tmdb.discover()
        self.assertTrue(int(response.status_code) == 200)
        data = json.loads(response.data.decode())
        self.assertTrue(isinstance(data['results'], list))
        # TODO check if all the shows are in the good format


if __name__ == '__main__':
    unittest.main()
