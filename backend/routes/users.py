from flask import Blueprint, jsonify, request

from backend.db import Db
from backend.models.user import User

# required line at the top of every blueprint file
users = Blueprint("users", __name__)  # match variable name and first arg to file name


@users.get("/")
def get_users():
    response = jsonify(User.query.all())
    return response


@users.post("/")
def post_users():
    db_session = Db.get_session()
    data = request.get_json()

    # Check if user already exists
    u = db_session.query(User).filter_by(username=data['username']).first()

    if u:
        # User exists, update their information
        u.username = data['username']
    else:
        # User does not exist, create a new one
        u = User(data['username'])
        db_session.add(u)

    db_session.commit()
    return jsonify(u)