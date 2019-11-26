# project/server/middlewares/auth.py
from flask import request, make_response, jsonify
from functools import wraps

from project.server.models import User

def with_authorization_middleware(fn):
    """
    Checks if there's an Authorization header in the request and supplies the valid user to the function (view)
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return fn(*args, **kwargs, user=None)
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                return fn(*args, **kwargs, user=user)
            return fn(*args, **kwargs, user=None)
        else:
            return fn(*args, **kwargs, user=None)

    return wrapper

def auth_middleware(fn):
    """
    Checks if there's an Authorization header in the request and supplies the valid user to the function (view)
    Aborts if there's any problem with the header (user must be logged in)
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                response_object = {
                    'status': 'fail',
                    'status_code': 401,
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(response_object)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                return fn(*args, **kwargs, user=user)
            response_object = {
                'status': 'fail',
                'status_code': 401,
                'message': resp
            }
            return make_response(jsonify(response_object)), 401
        else:
            response_object = {
                'status': 'fail',
                'status_code': 401,
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(response_object)), 401

    return wrapper