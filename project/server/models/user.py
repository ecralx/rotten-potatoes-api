# project/server/models/user.py

import jwt
import datetime

from project.server import app, db, bcrypt
from .blacklistToken import BlacklistToken
from .favourite import Favourite


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    favourites = db.relationship(lambda: Favourite, backref='user')

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def add_favourite(self, tmdb_id):
        """
        Adds a favourite show to the user
        :param tmdb_id:
        """
        is_already_in_favs = len([favourite for favourite in self.favourites if favourite.tmdb_id == int(tmdb_id)]) > 0
        if (not is_already_in_favs):
            favourite = Favourite(user_id = int(self.id), tmdb_id = int(tmdb_id))
            self.favourites.append(favourite)
        else:
            raise Exception('Cannot remove an inexistant favourite')

    def remove_favourite(self, tmdb_id):
        """
        Removes a favourite show to the user
        :param tmdb_id:
        """
        is_already_in_favs = len([favourite for favourite in self.favourites if favourite.tmdb_id == int(tmdb_id)]) > 0
        if (is_already_in_favs):
            self.favourites = [favourite for favourite in self.favourites if favourite.tmdb_id != int(tmdb_id) ]
        else:
            raise Exception('Cannot remove an inexistant favourite')
