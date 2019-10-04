# project/server/models/tmdb.py

import os

from urllib import request, parse
from urllib.error import HTTPError

class Response():
    """
        We define here a global http response object because HTTPError, HTTPResponse and our proper responses
        are different in the attributes naming.
        ie, for the status code, we have respectively, `obj.status`, `obj.code` and `obj.status_code`..
        For now, we have the following attributes: 
            - status_code (mandatory - int)
            - data (mandatory - bytes string)
    """
    def __init__(self, status_code, data):
        self._status_code = status_code
        self._data = data

    @property
    def status_code(self):
        return int(self._status_code)
    
    @property
    def data(self):
        return self._data
    

class Api():
    
    @staticmethod
    def parse_http_response_object(response):
        data = response.read()
        status_code = response.status
        return Response(status_code, data)

    @staticmethod
    def parse_http_error(error):
        data = error.reason.encode()
        status_code = error.code
        return Response(status_code, data)
    
class Tmdb():
    
    base_url = 'https://api.themoviedb.org/3/'
    
    @staticmethod
    def discover(page = 1):
        endpoint = 'discover/tv'
        params = {
            'page': page,
            'api_key': os.getenv('TMDB_API_KEY')
        }
        query_string = parse.urlencode(params)
        url = Tmdb.base_url + endpoint + "?" + query_string
        try:
            return Api.parse_http_response_object(request.urlopen(url))
        except HTTPError as e:
            return Api.parse_http_error(e)
        except:
            message = 'Sorry we couldn\'t reach the TMDB API..'
            return Response(500, message.encode)