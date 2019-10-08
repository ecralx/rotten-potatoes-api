# project/server/show/views.py

import json

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Tmdb, Show

show_blueprint = Blueprint('show', __name__)

class DiscoverAPI(MethodView):
    """
    Discover tv shows resource
    """

    def get(self):
        try:
            requested_page = request.args.get('page', default = 1, type = int)
            response = Tmdb.discover(page = requested_page)
            response_object = Tmdb.convert_to_response_object(response)
            return make_response(jsonify(response_object)), 200
        except:
            response_object = {
                'status': 'fail',
                'message': 'Failed to communicate with the tmdb API'
            }
            return make_response(jsonify(response_object)), 500

class SearchAPI(MethodView):
    """
    Search tv shows resource
    """

    def get(self):
        try:
            requested_query = request.args.get('query', type = str)
            requested_page = request.args.get('page', default = 1, type = int)
            response = Tmdb.search(query = requested_query, page = requested_page)
            response_object = Tmdb.convert_to_response_object(response)
            return make_response(jsonify(response_object)), 200
        except:
            response_object = {
                'status': 'fail',
                'message': 'Failed to communicate with the tmdb API'
            }
            return make_response(jsonify(response_object)), 500

# define the API resources
discover_view = DiscoverAPI.as_view('discover_api')
search_view = SearchAPI.as_view('search_api')

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