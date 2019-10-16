# project/server/auth/views.py


from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User, BlacklistToken
from project.server.middlewares import auth_middleware

user_blueprint = Blueprint('user', __name__)

class AddFavouriteAPI(MethodView):
    """
    Add favourite to a user Resource
    """
    @auth_middleware
    def post(self, user = None):
        # get the post data
        if (user):
            post_data = request.get_json()
            tmdb_id = post_data.get('tmdb_id')
            if (int(tmdb_id)):
                try:
                    user.add_favourite(tmdb_id)
                    db.session.commit()
                except Exception as e:
                    response_object = {
                        'status': 'fail',
                        'message': str(e)
                    }
                    return make_response(jsonify(response_object)), 500
                else:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully added the show.'
                    }
                    return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid TMDB id.'
                }
                return make_response(jsonify(response_object)), 500            
        else:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(response_object)), 500

class RemoveFavouriteAPI(MethodView):
    """
    Remove favourite from a user Resource
    """
    @auth_middleware
    def post(self, user = None):
        # get the post data
        if (user):
            post_data = request.get_json()
            tmdb_id = post_data.get('tmdb_id')
            if (int(tmdb_id)):
                try:
                    user.remove_favourite(tmdb_id)
                    db.session.commit()
                except Exception as e:
                    response_object = {
                        'status': 'fail',
                        'message': str(e)
                    }
                    return make_response(jsonify(response_object)), 500
                else:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully removed the show.'
                    }
                    return make_response(jsonify(response_object)), 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid TMDB id.'
                }
                return make_response(jsonify(response_object)), 500            
        else:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(response_object)), 500


# define the API resources
add_favourite_view = AddFavouriteAPI.as_view('add_favourite_api')
remove_favourite_view = RemoveFavouriteAPI.as_view('remove_favourite_api')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
        '/user/favourite/add',
        view_func=add_favourite_view,
        methods=['POST']
)
user_blueprint.add_url_rule(
        '/user/favourite/remove',
        view_func=remove_favourite_view,
        methods=['POST']
)