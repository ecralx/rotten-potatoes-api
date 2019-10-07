# project/server/models/tmdb.py

class Show():
    def __init__(self, tmdb_id, name, overview = None, poster_path = None, vote_average = None, original_language = None):
        self._tmdb_id = tmdb_id
        self._name = name
        self._overview = overview
        self._poster_path = poster_path
        self._vote_average = vote_average
        self._original_language = original_language

    @staticmethod
    def from_dict(show_dict):
        """ Create a show instance from a dict (generally taken from tmdb) """
        return Show(
            show_dict['id'] if show_dict['id'] else show_dict['tmdb_id'],
            show_dict['name'],
            show_dict['overview'],
            show_dict['poster_path'],
            show_dict['vote_average'],
            show_dict['original_language'],
        )

    def to_dict(self):
        return {
            'tmdb_id': self._tmdb_id,
            'name': self._name,
            'overview': self._overview,
            'poster_path': self._poster_path,
            'vote_average': self._vote_average,
            'original_language': self._original_language
        }
    
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
