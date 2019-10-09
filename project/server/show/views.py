# project/server/show/views.py

import json

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Tmdb, Show, Season

show_blueprint = Blueprint('show', __name__)

class DiscoverAPI(MethodView):
    """
    Discover tv shows resource
    """

    def get(self):
        requested_page = request.args.get('page', default = 1, type = int)
        try:
            response = Tmdb.discover(page = requested_page)
            response_object = Tmdb.convert_list_to_response_object(response)
            return make_response(jsonify(response_object)), 200
        except:
            response_object = {
                'status': 'fail',
                'message': 'Failed to communicate with the tmdb API.'
            }
            return make_response(jsonify(response_object)), 500

class SearchAPI(MethodView):
    """
    Search tv shows resource
    """

    def get(self):
        requested_query = request.args.get('query', type = str)
        requested_page = request.args.get('page', default = 1, type = int)
        if (requested_query):
            try:
                response = Tmdb.search(query = requested_query, page = requested_page)
                response_object = Tmdb.convert_list_to_response_object(response)
                return make_response(jsonify(response_object)), 200
            except:
                response_object = {
                    'status': 'fail',
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'message': 'You need to specify the searched term.'
            }
            return make_response(jsonify(response_object)), 404

class DetailAPI(MethodView):
    """
    Search tv shows resource
    """

    def get(self, tmdb_id):
        if (int(tmdb_id) > 0):
            try:
                response = Tmdb.detail(tmdb_id = int(tmdb_id))
                data = json.loads(response.data.decode())
                response_object = Show.from_dict(data).to_dict()
                return make_response(jsonify(response_object)), 200
            except:
                response_object = {
                    'status': 'fail',
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'message': 'The TMDB id specified is invalid.'
            }
            return make_response(jsonify(response_object)), 404

class SimilarAPI(MethodView):
    """
    Similar tv shows resource
    """

    def get(self, tmdb_id):
        requested_page = request.args.get('page', default = 1, type = int)
        if (int(tmdb_id) > 0):
            try:
                response = Tmdb.similar(tmdb_id = tmdb_id, page = requested_page)
                response_object = Tmdb.convert_list_to_response_object(response)
                return make_response(jsonify(response_object)), 200
            except:
                response_object = {
                    'status': 'fail',
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
                'message': 'The TMDB id specified is invalid.'
            }
            return make_response(jsonify(response_object)), 404

class SeasonAPI(MethodView):
    """
    Season (tv shows) resource
    """

    def get(self, tmdb_show_id, season_number):
        if (int(tmdb_show_id) > 0 and int(season_number) > 0):
            try:
                response = Tmdb.season(tmdb_show_id = tmdb_show_id, season_number = season_number)
                data = json.loads(response.data.decode())                
                response_object = Season.from_dict(data).to_dict()
                return make_response(jsonify(response_object)), 200
            except:
                response_object = {
                    'status': 'fail',
                    'message': 'Failed to communicate with the tmdb API.'
                }
                return make_response(jsonify(response_object)), 500
        else:
            response_object = {
                'status': 'fail',
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