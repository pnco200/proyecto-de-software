from flask import Blueprint, jsonify
from web.helpers.apivalidations import requires_auth
api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@api_user_bp.route('/profile')
@requires_auth()
def get_user_profile(user):
    profile = {
        "name": user.name,
        "email": user.email,
        "id": user.id,
        "lastname": user.lastname,
        "username": user.username,
    }
    return jsonify(profile), 200