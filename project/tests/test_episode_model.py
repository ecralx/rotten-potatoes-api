# project/tests/test_episode_model.py


import unittest
import json

from project.server import db
from project.server.models import Episode
from project.tests.base import BaseTestCase

# from a season response
MOCKED_TMDB_RESPONSE = json.loads("{\"air_date\":\"2011-04-17\",\"crew\":[{\"id\":44797,\"credit_id\":\"5256c8a219c2956ff6046e77\",\"name\":\"Tim Van Patten\",\"department\":\"Directing\",\"job\":\"Director\",\"profile_path\":\"/6b7l9YbkDHDOzOKUFNqBVaPjcgm.jpg\"},{\"id\":1318704,\"credit_id\":\"54eef2429251417974005cb6\",\"name\":\"Alik Sakharov\",\"department\":\"Camera\",\"job\":\"Director of Photography\",\"profile_path\":\"/50ZlHkh66aOPxQMjQ21LJDAkYlR.jpg\"},{\"id\":18077,\"credit_id\":\"54eef2ab925141795f005d4f\",\"name\":\"Oral Norrie Ottey\",\"department\":\"Editing\",\"job\":\"Editor\",\"profile_path\":null},{\"id\":9813,\"credit_id\":\"5256c8a019c2956ff6046e2b\",\"name\":\"David Benioff\",\"department\":\"Writing\",\"job\":\"Writer\",\"profile_path\":\"/8CuuNIKMzMUL1NKOPv9AqEwM7og.jpg\"},{\"id\":228068,\"credit_id\":\"5256c8a219c2956ff6046e4b\",\"name\":\"D. B. Weiss\",\"department\":\"Writing\",\"job\":\"Writer\",\"profile_path\":\"/caUAtilEe06OwOjoQY3B7BgpARi.jpg\"}],\"episode_number\":1,\"guest_stars\":[{\"id\":117642,\"name\":\"Jason Momoa\",\"credit_id\":\"5256c8a219c2956ff6046f40\",\"character\":\"Khal Drogo\",\"order\":0,\"profile_path\":\"/PSK6GmsVwdhqz9cd1lwzC6a7EA.jpg\"},{\"id\":946696,\"name\":\"Ian Whyte\",\"credit_id\":\"5750cd459251412b0f000224\",\"character\":\"White Walker\",\"order\":46,\"profile_path\":\"/6mRY7hTtHfDTGuTLmZmODOu9buF.jpg\"},{\"id\":438859,\"name\":\"Susan Brown\",\"credit_id\":\"57520bc19251414c470000de\",\"character\":\"Septa Mordane\",\"order\":52,\"profile_path\":\"/5bYvoJDOw4okAzSxJ1avXweUyA9.jpg\"},{\"id\":1833,\"name\":\"Jamie Sives\",\"credit_id\":\"5752136f9251414c510001a0\",\"character\":\"Jory Cassel\",\"order\":55,\"profile_path\":\"/92BcXrr2W7gZri6xVlLhpLLaPsf.jpg\"},{\"id\":234907,\"name\":\"Dar Salim\",\"credit_id\":\"5752158b9251414c470001c0\",\"character\":\"Qotho\",\"order\":56,\"profile_path\":\"/3CrPTwZJ0hsWzX7oi7sKFfzDo82.jpg\"},{\"id\":11279,\"name\":\"Roger Allam\",\"credit_id\":\"575216bdc3a36851fe0001d8\",\"character\":\"Illyrio Mopatis\",\"order\":57,\"profile_path\":\"/gr59GfVZz9QV6jZyHKOsKCBxXPr.jpg\"},{\"id\":1600544,\"name\":\"Aimee Richardson\",\"credit_id\":\"57521d4cc3a3685215000344\",\"character\":\"Myrcella Baratheon\",\"order\":60,\"profile_path\":\"/r53KnAfLiR8NaK3Kp2Nu4q0KSoP.jpg\"},{\"id\":1600543,\"name\":\"Callum Wharry\",\"credit_id\":\"57521fafc3a368521500041d\",\"character\":\"Tommen Baratheon\",\"order\":61,\"profile_path\":\"/rVaMQfGwylZWWM2eRJ3qAEkS0tK.jpg\"}],\"name\":\"Winter Is Coming\",\"overview\":\"Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.\",\"id\":63056,\"production_code\":\"101\",\"season_number\":1,\"still_path\":\"/wrGWeW4WKxnaeA8sxJb2T9O6ryo.jpg\",\"vote_average\":7.11904761904762,\"vote_count\":21}")

MOCKED_TO_DICT = {
    'tmdb_id': 63056,
    'season_number': 1,
    'episode_number': 1,
    'air_date': '2011-04-17',
    'name': 'Winter Is Coming',
    'overview': 'blablabla'
}

class TestEpisodeModel(BaseTestCase):
    """
    Testing the Episode model's behaviour
    """

    def test_episode_from_dict(self):
        episode = Episode.from_dict(MOCKED_TMDB_RESPONSE)
        self.assertEqual(episode.tmdb_id, 63056)
        self.assertEqual(episode.season_number, 1)
        self.assertEqual(episode.episode_number, 1)
        self.assertEqual(episode.air_date, '2011-04-17')
        self.assertEqual(episode.name, 'Winter Is Coming')
        self.assertEqual(episode.overview, "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.")

    def test_episode_to_dict(self):
        season = Episode(
            63056,
            1,
            1,
            '2011-04-17',
            'Winter Is Coming',
            'blablabla'
        )
        self.assertDictEqual(season.to_dict(), MOCKED_TO_DICT)



if __name__ == '__main__':
    unittest.main()
