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
            response = Tmdb.discover()
            data = json.loads(response.data.decode())
            page = data['page']
            total_results = data['total_results']
            total_pages = data['total_pages']
            shows = [Show.from_dict(show).to_dict() for show in data['results']]
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'results': shows,
                'page': page,
                'total_results': total_results,
                'total_pages': total_pages,
            }
            return make_response(jsonify(response_object)), 200
        except:
            response_object = {
                'status': 'fail',
                'message': 'Failed to communicate with the tmdb API'
            }
            return make_response(jsonify(response_object)), 500

# define the API resources
discover_view = DiscoverAPI.as_view('discover_api')

# add Rules for API Endpoints
show_blueprint.add_url_rule(
    '/show/discover',
    view_func=discover_view,
    methods=['GET']
)
