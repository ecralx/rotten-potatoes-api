# project/server/models/favourite.py

import json

from project.server import app, db
from .tmdb import Tmdb
from .show import Show

class Favourite(db.Model):
    """ Favourite (show) Model for storing favourite shows for a user """
    __tablename__ = "favourites"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    tmdb_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, tmdb_id):
        self.user_id = user_id
        self.tmdb_id = tmdb_id

    def get_show(self):
        """
        Get the show object from a favourite
        :return: Show
        """
        response = Tmdb.detail(tmdb_id = self.tmdb_id)
        if (response):
            data = response.json()
            return Show.from_dict(data)
        else:
            raise Exception('Could\'nt reach the server')