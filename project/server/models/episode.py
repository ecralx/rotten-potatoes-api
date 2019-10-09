# project/server/models/episode.py

class Episode():

    def __init__(self, tmdb_id, season_number, episode_number, air_date, name = None, overview = None):
        self._tmdb_id = tmdb_id
        self._season_number = season_number
        self._episode_number = episode_number
        self._air_date = air_date
        self._name = name
        self._overview = overview
    
    @staticmethod
    def from_dict(episode_dict = {}):
        """ Create a show instance from a dict (generally taken from tmdb) """        
        return Episode(
            episode_dict['id'] if episode_dict.get('id') else episode_dict['tmdb_id'],
            episode_dict['season_number'],
            episode_dict['episode_number'],
            episode_dict['air_date'],
            episode_dict['name'],
            episode_dict['overview']
        )

    def to_dict(self):
        """ Return all non empty attributes as a dict """
        attributes = {
            'tmdb_id': self._tmdb_id,
            'season_number': self._season_number,
            'episode_number': self._episode_number,
            'air_date': self._air_date,
            'name': self._name,
            'overview': self._overview
        }
        return {key: value for key,value in attributes.items() if value}

    @property
    def tmdb_id(self):
        return self._tmdb_id
    
    @property
    def season_number(self):
        return self._season_number

    @property
    def episode_number(self):
        return self._episode_number

    @property
    def air_date(self):
        return self._air_date

    @property
    def name(self):
        return self._name

    @property
    def overview(self):
        return self._overview