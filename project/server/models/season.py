# project/server/models/season.py

from .episode import Episode

class Season():

    def __init__(self, tmdb_id, season_number, name = None, overview = None, poster_path = None, air_date = None, episodes = []):
        self._tmdb_id = tmdb_id
        self._season_number = season_number
        self._name = name
        self._overview = overview
        self._poster_path = poster_path
        self._air_date = air_date
        self._episodes = episodes

    @staticmethod
    def from_dict(season_dict = {}):
        return Season(
            season_dict['id'] if season_dict.get('id') else season_dict['tmdb_id'],
            season_dict['season_number'],
            season_dict['name'],
            season_dict['overview'],
            season_dict['poster_path'],
            season_dict['air_date'],
            [Episode.from_dict(episode_dict) for episode_dict in season_dict['episodes']] if season_dict.get('episodes') else []
        )

    def to_dict(self):
        attributes = {
            'tmdb_id': self._tmdb_id,
            'season_number': self._season_number,
            'name': self._name,
            'overview': self._overview,
            'poster_path': self._poster_path,
            'air_date': self._air_date,
            'episodes': [episode.to_dict() for episode in self._episodes]
        }
        return {key: value for key,value in attributes.items() if value}

    @property
    def tmdb_id(self):
        return int(self._tmdb_id)
    
    @property
    def season_number(self):
        return int(self._season_number)
        
    @property
    def name(self):
        return self._name

    @property
    def overview(self):
        return self._overview
    
    @property
    def poster_path(self):
        return self._poster_path
        
    @property
    def air_date(self):
        return self._air_date
        
    @property
    def episodes(self):
        return self._episodes