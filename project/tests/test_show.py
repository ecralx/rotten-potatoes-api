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
            self.assertTrue(data['results'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()