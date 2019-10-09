# project/tests/test_show_model.py


import unittest
import json

from project.server import db
from project.server.models import Season
from project.tests.base import BaseTestCase


MOCKED_TMDB_RESPONSE = json.loads('{"_id":"587bea9bc3a368494c0116e6","air_date":"2008-04-05","episodes":[{"air_date":"2008-04-05","episode_number":1,"id":1257560,"name":"Final Rescue Approved: Explosive Suppression Complete!","overview":"The series begins!","production_code":"","season_number":1,"show_id":69700,"still_path":null,"vote_average":0.0,"vote_count":0,"crew":[],"guest_stars":[]}],"name":"Tomica Hero: Rescue Force","overview":"","id":83995,"poster_path":null,"season_number":1}')

MOCKED_TO_DICT = {
    'tmdb_id': 83995,
    'season_number': 1,
    'name': 'Tomica Hero: Rescue Force',
    'overview': 'fdsqfqdsfsqd',
    'poster_path': '/dsfsqdfdsqfqdsfsqdfdsqfqdsfsqd.jpg',
    'air_date': '2008-04-05',
}

class TestSeasonModel(BaseTestCase):
    """
    Testing the Season model's behaviour
    """

    def test_season_from_dict(self):
        season = Season.from_dict(MOCKED_TMDB_RESPONSE)
        self.assertEqual(season.tmdb_id, 83995)
        self.assertEqual(season.season_number, 1)
        self.assertEqual(season.name, 'Tomica Hero: Rescue Force')
        self.assertEqual(season.overview, '')
        self.assertEqual(season.poster_path, None)
        self.assertEqual(season.air_date, '2008-04-05')
        self.assertEqual(len(season.episodes), 1)

    def test_season_to_dict(self):
        season = Season(
            83995,
            1,
            'Tomica Hero: Rescue Force',
            'fdsqfqdsfsqd',
            '/dsfsqdfdsqfqdsfsqdfdsqfqdsfsqd.jpg',
            '2008-04-05'
        )
        self.assertDictEqual(season.to_dict(), MOCKED_TO_DICT)



if __name__ == '__main__':
    unittest.main()
