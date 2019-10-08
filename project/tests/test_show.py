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
                '/show/discover?page=2',
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['page'])
            self.assertEqual(int(data['page']), 2)
            self.assertTrue(data['total_results'])
            self.assertTrue(data['total_pages'])
            for show in data['results']:
                self.assertTrue(show['name'])
                self.assertTrue(show['tmdb_id'])

    def test_search(self):
        """ Testing shows search """
        with self.client:
            response = self.client.get(
                '/show/search?query=ozark&page=2'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['page'])
            self.assertEqual(int(data['page']), 2)
            self.assertTrue(data['total_results'])
            self.assertTrue(data['total_pages'])
            for show in data['results']:
                self.assertTrue(show['name'])
                self.assertTrue(show['tmdb_id'])

    def test_detail(self):
        """ Testing show's details """
        with self.client:
            response = self.client.get(
                '/show/69740'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['name'], 'Ozark')
            self.assertTrue(data['overview'])
            self.assertTrue(data['poster_path'])
            self.assertTrue(data['vote_average'])
            self.assertEqual(data['original_language'], 'en')


if __name__ == '__main__':
    unittest.main()