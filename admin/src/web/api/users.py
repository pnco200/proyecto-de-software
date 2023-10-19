from flask import Blueprint, jsonify
from web.helpers.auth import requires_auth

api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@requires_auth
@api_user_bp.route('/profile')
def get_user_profile(user):
    return jsonify(user), 200