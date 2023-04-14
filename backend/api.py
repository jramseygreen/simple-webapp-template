from flask import Blueprint, jsonify, request
from flask_cors import CORS

from .routes.users import users

# required line at the top of every blueprint file
api = Blueprint("api", __name__)  # match variable name and first arg to file name
# register more blueprints here to further split up the api
# e.g.
# api.register_blueprint(blueprint, url_prefix='/users')
# would cascade through /api/users

api.register_blueprint(users, url_prefix='/users')

CORS(api) # removes cors policy for all api routes

# api routes when hitting /api
@api.route("/")
def heartbeat():
    return jsonify({"status": "healthy"})
