# project/tests/test_user_model.py


import unittest

from project.server import db
from project.server.models import User
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(
            auth_token.decode("utf-8") ) == 1)

    def test_add_favourite(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        user.add_favourite(tmdb_id=69740)
        favourites = user.favourites
        favourite = favourites.pop()
        self.assertEqual(favourite.user_id, 1)
        self.assertEqual(favourite.tmdb_id, 69740)
    
    def test_remove_favourite(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        user.add_favourite(tmdb_id=69740)
        user.remove_favourite(tmdb_id=69740)
        favourites = user.favourites
        self.assertTrue(len([favourite for favourite in favourites if favourite.tmdb_id == 69740]) == 0)


if __name__ == '__main__':
    unittest.main()
