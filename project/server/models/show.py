# project/server/models/show.py

from .season import Season
from .episode import Episode
from .genre import Genre

class Show():

    def __init__(self, tmdb_id, name, overview = None, poster_path = None, vote_average = None,
        original_language = None, seasons = [], genres = [], next_episode_to_air = None):
        self._tmdb_id = tmdb_id
        self._name = name
        self._overview = overview
        self._poster_path = poster_path
        self._vote_average = vote_average
        self._original_language = original_language
        self._seasons = seasons
        self._genres = genres
        self._next_episode_to_air = next_episode_to_air

    @staticmethod
    def from_dict(show_dict = {}):
        """ Create a show instance from a dict (generally taken from tmdb) """
        return Show(
            show_dict['id'] if show_dict.get('id') else show_dict['tmdb_id'],
            show_dict['name'],
            show_dict['overview'],
            show_dict['poster_path'],
            show_dict['vote_average'],
            show_dict['original_language'],
            [Season.from_dict(season_dict) for season_dict in show_dict['seasons']] if show_dict.get('seasons') else [],
            [Genre.from_dict(genre_dict) for genre_dict in show_dict['genres']] if show_dict.get('seasons') else [],
            Episode.from_dict(show_dict['next_episode_to_air']) if show_dict.get('next_episode_to_air') else None
        )

    def to_dict(self):
        """ Return all non empty attributes as a dict """
        attributes = {
            'tmdb_id': self._tmdb_id,
            'name': self._name,
            'overview': self._overview,
            'poster_path': self._poster_path,
            'vote_average': self._vote_average,
            'original_language': self._original_language,
            'seasons': [season.to_dict() for season in self._seasons],
            'genres': [genre.to_dict() for genre in self._genres],
            'next_episode_to_air': self._next_episode_to_air.to_dict() if self._next_episode_to_air else False
        }
        return {key: value for key,value in attributes.items() if value}
    
    @property
    def tmdb_id(self):
        return int(self._tmdb_id)

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
    def vote_average(self):
        return self._vote_average

    @property
    def original_language(self):
        return self._original_language

    @property
    def seasons(self):
        return self._seasons

    @property
    def genres(self):
        return self._genres

    @property
    def next_episode_to_air(self):
        return self._next_episode_to_air
