# project/server/show/views.py

import json

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Tmdb, Show, Season
from project.server.middlewares import with_authorization_middleware

show_blueprint = Blueprint('show', __name__)

class DiscoverAPI(MethodView):
    """
    Discover tv shows resource
    """
    @with_authorization_middleware
    def get(self, user=None):
        requested_page = request.args.get('page', default = 1, type = int)
        requested_genres = request.args.get('genres', default = '', type = str)
        response = Tmdb.discover(page = requested_page, genres = requested_genres)
        if (response):
            response_object = Tmdb.convert_list_to_response_object(response, user)
            return make_response(jsonify(response_object)), 200
        else:
            response_object = {
                'status': 'fail',
                'status_code': 500,
                'message': 'Failed to communicate with the tmdb API.'
            }
            return make_response(jsonify(response_object)), 500

class SearchAPI(MethodView):
    """
    Search tv shows resource
    """
    
    @with_authorization_middleware
    def get(self, user=None):
        requested_query = request.args.get('query', type = str)
        requested_page = request.args.get('page', default = 1, type = int)
        requested_genres = request.args.get('genres', default = '', type = str)
        if (requested_query):
            response = Tmdb.search(query = requested_query, page = requested_page, genres = requested_genres)
            if (response):
                response_object = Tmdb.convert_list_to_response_object(response, user)
                return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'status_code': 500,
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500    
        else:
            response_object = {
                'status': 'fail',
                'status_code': 404,
                'message': 'You need to specify the searched term.'
            }
            return make_response(jsonify(response_object)), 404

class DetailAPI(MethodView):
    """
    Search tv shows resource
    """
    @with_authorization_middleware
    def get(self, tmdb_id, user=None):
        if (((isinstance(tmdb_id, str) and tmdb_id.isdecimal()) or (isinstance(tmdb_id, int))) and int(tmdb_id) > 0):
            response = Tmdb.detail(tmdb_id = int(tmdb_id))
            if (response):
                data = response.json()
                response_object = Show.from_dict(data).to_dict()
                response_object['is_liked'] = user.has_favourite(tmdb_id)
                response_object['status_code'] = 200
                return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'status_code': 500,
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'status_code': 404,
                'message': 'The TMDB id specified is invalid.'
            }
            return make_response(jsonify(response_object)), 404

class SimilarAPI(MethodView):
    """
    Similar tv shows resource
    """
    @with_authorization_middleware
    def get(self, tmdb_id, user=None):
        requested_page = request.args.get('page', default = 1, type = int)
        if (((isinstance(tmdb_id, str) and tmdb_id.isdecimal()) or (isinstance(tmdb_id, int))) and int(tmdb_id) > 0):
            response = Tmdb.similar(tmdb_id = tmdb_id, page = requested_page)
            if (response):
                response_object = Tmdb.convert_list_to_response_object(response, user)
                return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'status_code': 500,
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'status_code': 404,
                'message': 'The TMDB id specified is invalid.'
            }
            return make_response(jsonify(response_object)), 404

class SeasonAPI(MethodView):
    """
    Season (tv shows) resource
    """

    def get(self, tmdb_show_id, season_number):
        if (((isinstance(tmdb_show_id, str) and tmdb_show_id.isdecimal()) or (isinstance(tmdb_show_id, int))) and ((isinstance(season_number, str) and season_number.isdecimal()) or (isinstance(season_number, int))) and int(tmdb_show_id) > 0):
            response = Tmdb.season(tmdb_show_id = tmdb_show_id, season_number = season_number)
            if (response):
                data = response.json()
                response_object = Season.from_dict(data).to_dict()
                response_object['status_code'] = 200
                return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'status_code': 505,
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'status_code': 404,
                'message': 'The TMDB id or the season number specified is invalid.'
            }
            return make_response(jsonify(response_object)), 404



# define the API resources
discover_view = DiscoverAPI.as_view('discover_api')
search_view = SearchAPI.as_view('search_api')
detail_view = DetailAPI.as_view('detail_api')
similar_view = SimilarAPI.as_view('similar_api')
season_view = SeasonAPI.as_view('season_api')

# add Rules for API Endpoints
show_blueprint.add_url_rule(
    '/show/discover',
    view_func=discover_view,
    methods=['GET']
)
show_blueprint.add_url_rule(
    '/show/search',
    view_func=search_view,
    methods=['GET']
)
show_blueprint.add_url_rule(
    '/show/<tmdb_id>',
    view_func=detail_view,
    methods=['GET']
)
show_blueprint.add_url_rule(
    '/show/<tmdb_id>/similar',
    view_func=similar_view,
    methods=['GET']
)
show_blueprint.add_url_rule(
    '/show/<tmdb_show_id>/season/<season_number>',
    view_func=season_view,
    methods=['GET']
)