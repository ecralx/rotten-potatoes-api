# project/tests/test_show.py

import unittest
import json

from project.server.models import User
from project.tests.base import BaseTestCase


class TestShowBlueprint(BaseTestCase):
    
    def test_discover(self):
        """ Testing shows discovery """
        with self.client:
            response = self.client.get(
                '/show/discover',
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['page'])
            self.assertTrue(data['total_results'])
            self.assertTrue(data['total_pages'])
            for show in data['results']:
                self.assertTrue(show['name'])
                self.assertTrue(show['tmdb_id'])


if __name__ == '__main__':
    unittest.main()