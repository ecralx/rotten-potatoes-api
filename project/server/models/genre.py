# project/server/models/genre.py

class Genre():

    def __init__(self, tmdb_id, name):
        self._tmdb_id = tmdb_id
        self._name = name
    
    @staticmethod
    def from_dict(genre_dict):
        """ Create a genre instance from a dict (generally taken from tmdb) """        
        return Genre(
            genre_dict['id'] if genre_dict.get('id') else genre_dict['tmdb_id'],
            genre_dict['name']
        )

    def to_dict(self):
        """ Return all non empty attributes as a dict """
        attributes = {
            'tmdb_id': self._tmdb_id,
            'name': self._name,
        }
        return {key: value for key,value in attributes.items() if value}

    @property
    def tmdb_id(self):
        return int(self._tmdb_id)

    @property
    def name(self):
        return int(self._name)