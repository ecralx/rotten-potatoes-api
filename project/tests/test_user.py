# project/tests/test_user.py

import unittest
import json

from project.server.models import User
from project.tests.base import BaseTestCase
from project.tests.test_auth import register_user, login_user

def add_favourite(self, tmdb_id, authorization):
    return self.client.post(
        '/user/favourite/add',
        data=json.dumps({
            'tmdb_id': tmdb_id
        }),
        headers={
            'Authorization': 'Bearer ' + authorization
        },
        content_type='application/json'
    )

def remove_favourite(self, tmdb_id, authorization):
    return self.client.post(
        '/user/favourite/remove',
        data=json.dumps({
            'tmdb_id': tmdb_id
        }),
        headers={
            'Authorization': 'Bearer ' + authorization
        },
        content_type='application/json'
    )

class TestUserBlueprint(BaseTestCase):
    
    def test_add_favourite(self):
        """ Testing API's add a favourite """
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', '123456')
            response = add_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)

    def test_add_favourite_with_already_added_favourite(self):
        """ Testing API's add a favourite when the show was already added to favourites """
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', '123456')
            add_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            response = add_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertEqual(response.status_code, 500)
          
    def test_remove_favourite(self):
        """ Testing API's remove a favourite """
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', '123456')
            add_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            response = remove_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)

    def test_remove_favourite_with_not_added_favourite(self):
        """ Testing API's remove a favourite when the show wasn't added to favourites """
        with self.client:
            resp_register = register_user(self, 'joe@gmail.com', '123456')
            response = remove_favourite(self, 69740, json.loads(
                resp_register.data.decode()
            )['auth_token'])
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertEqual(response.status_code, 500)

    


if __name__ == '__main__':
    unittest.main()