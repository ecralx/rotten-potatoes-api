# project/server/models/tmdb.py

import os
import json
import requests

from .show import Show

class Tmdb():
    
    base_url = 'https://api.themoviedb.org/3/'
    
    @staticmethod
    def convert_list_to_response_object(response, user=None):
        data = response.json()
        page = data['page']
        total_results = data['total_results']
        total_pages = data['total_pages']
        shows = [Show.from_dict(show).to_dict() for show in data['results']]
        if (user):
            for show in shows:
                show['is_liked'] = user.has_favourite(show.get('tmdb_id'))
        return {
            'status_code': 200,
            'status': 'success',
            'message': 'Successfully got the shows.',
            'results': shows,
            'page': page,
            'total_results': total_results,
            'total_pages': total_pages,
        }

    @staticmethod
    def discover(page = 1):
        endpoint = 'discover/tv'
        params = {
            'page': page,
            'api_key': os.getenv('TMDB_API_KEY')
        }
        url = Tmdb.base_url + endpoint + "?"
        return requests.get(url, params=params)

    @staticmethod
    def search(query, page = 1):
        endpoint = 'search/tv'
        params = {
            'query': query,
            'page': page,
            'api_key': os.getenv('TMDB_API_KEY')
        }
        url = Tmdb.base_url + endpoint + "?"
        return requests.get(url, params=params)

    @staticmethod
    def detail(tmdb_id):
        endpoint = 'tv/{}'.format(tmdb_id)
        params = {
            'api_key': os.getenv('TMDB_API_KEY')
        }
        url = Tmdb.base_url + endpoint + "?"
        return requests.get(url, params=params)
    
    @staticmethod
    def similar(tmdb_id, page = 1):
        endpoint = 'tv/{}/similar'.format(tmdb_id)
        params = {
            'page': page,
            'api_key': os.getenv('TMDB_API_KEY')
        }
        url = Tmdb.base_url + endpoint + "?"
        return requests.get(url, params=params)
        
    @staticmethod
    def season(tmdb_show_id, season_number):
        endpoint = 'tv/{}/season/{}'.format(tmdb_show_id, season_number)
        params = {
            'api_key': os.getenv('TMDB_API_KEY')
        }
        url = Tmdb.base_url + endpoint + "?"
        return requests.get(url, params=params)