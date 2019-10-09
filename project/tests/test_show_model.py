# project/tests/test_show_model.py


import unittest
import json

from project.server import db
from project.server.models import Show
from project.tests.base import BaseTestCase


MOCKED_TMDB_RESPONSE = json.loads('{"backdrop_path":"/fY5QzzuTquAJCkW5kaunZeb6Ney.jpg","created_by":[{"id":1281388,"credit_id":"589d4676c3a3685f970029be","name":"Bill Dubuque","gender":2,"profile_path":"/nPiWslnfdaWuiSlX1K8gpX5ogzh.jpg"},{"id":1318813,"credit_id":"589d46b99251412cc60027ad","name":"Mark Williams","gender":2,"profile_path":null}],"episode_run_time":[80,56],"first_air_date":"2017-07-21","genres":[{"id":80,"name":"Crime"},{"id":18,"name":"Drama"}],"homepage":"https://www.netflix.com/title/80117552","id":69740,"in_production":true,"languages":["en"],"last_air_date":"2018-08-31","last_episode_to_air":{"air_date":"2018-08-31","episode_number":10,"id":1560793,"name":"The Gold Coast","overview":"Marty makes plans without telling Wendy. Darlene sends a message via Jonah. Wyatt learns the truth about his dad. Ruth realizes Cade must be stopped.","production_code":"","season_number":2,"show_id":69740,"still_path":"/xI3NAcU3G2wDaKgndwaNqfQlcuw.jpg","vote_average":7.0,"vote_count":3},"name":"Ozark","next_episode_to_air":null,"networks":[{"name":"Netflix","id":213,"logo_path":"/wwemzKWzjKYJFfCeiB57q3r4Bcm.png","origin_country":""}],"number_of_episodes":20,"number_of_seasons":2,"origin_country":["US"],"original_language":"en","original_name":"Ozark","overview":"A financial adviser drags his family from Chicago to the Missouri Ozarks, where he must launder $500 million in five years to appease a drug boss.","popularity":35.707,"poster_path":"/pCGyPVrI9Fzw6rE1Pvi4BIXF6ET.jpg","production_companies":[{"id":2531,"logo_path":"/pC2iDCDCvV85vOBP7a5Ukxuc0Du.png","name":"Media Rights Capital","origin_country":"US"},{"id":5357,"logo_path":"/19A0Ilxeh1bWMlyMtMgGzcNBn07.png","name":"Zero Gravity Management","origin_country":"US"}],"seasons":[{"air_date":"2017-07-21","episode_count":10,"id":84057,"name":"Season 1","overview":"","poster_path":"/x7M93pIs7spQRLjtcNra1dDemxx.jpg","season_number":1},{"air_date":"2018-08-31","episode_count":10,"id":105425,"name":"Season 2","overview":"Marty\'s plan to open a riverboat casino is complicated by Darlene Snell\'s schemes, Ruth\'s paroled father, state politics and a Kansas City mobster.","poster_path":"/pXAR26dF40FTJc6TkfALlnRGxcT.jpg","season_number":2}],"status":"Returning Series","type":"Scripted","vote_average":7.9,"vote_count":411}')

MOCKED_TO_DICT = {
    'tmdb_id': 69740,
    'name': 'Ozark',
    'overview': 'A financial adviser drags his family from Chicago to the Missouri Ozarks, where he must launder $500 million in five years to appease a drug boss.',
    'poster_path': '/pCGyPVrI9Fzw6rE1Pvi4BIXF6ET.jpg',
    'vote_average': 7.9,
    'original_language': 'en',
}

class TestShowModel(BaseTestCase):
    """
    Testing the Show model's behaviour
    """

    def test_show_from_dict(self):
        show = Show.from_dict(MOCKED_TMDB_RESPONSE)
        self.assertEqual(show.name, 'Ozark')
        self.assertEqual(len(show.genres), 2)
        self.assertEqual(show.next_episode_to_air, None)
        self.assertEqual(show.original_language, 'en')
        self.assertEqual(show.overview, 'A financial adviser drags his family from Chicago to the Missouri Ozarks, where he must launder $500 million in five years to appease a drug boss.')
        self.assertEqual(show.poster_path, '/pCGyPVrI9Fzw6rE1Pvi4BIXF6ET.jpg')
        self.assertEqual(len(show.seasons), 2)
        self.assertEqual(show.vote_average, 7.9)

    def test_show_to_dict(self):
        show = Show(
            69740,
            'Ozark',
            'A financial adviser drags his family from Chicago to the Missouri Ozarks, where he must launder $500 million in five years to appease a drug boss.',
            '/pCGyPVrI9Fzw6rE1Pvi4BIXF6ET.jpg',
            7.9,
            'en',
        )
        self.assertDictEqual(show.to_dict(), MOCKED_TO_DICT)



if __name__ == '__main__':
    unittest.main()
