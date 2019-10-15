# project/tests/test_favourite_model.py


import unittest

from project.server import db
from project.server.models import User, Favourite
from project.tests.base import BaseTestCase


class TestFavouriteModel(BaseTestCase):

    def test_get_show(self):
        user = User(
            email = 'test@test.com',
            password = 'allo'   
        )
        db.session.add(user)
        db.session.commit()
        user.add_favourite(tmdb_id=69740)
        favourites = user.favourites
        favourite = favourites.pop()
        show = favourite.get_show()
        self.assertEqual(show.name, 'Ozark')