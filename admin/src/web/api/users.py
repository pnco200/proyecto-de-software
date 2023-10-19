from flask import Blueprint, jsonify
from web.helpers.apivalidations import requires_auth

api_user_bp = Blueprint("user_api", __name__, url_prefix="/api/me/")

@api_user_bp.route('/profile')
@requires_auth()
def get_user_profile():
    return jsonify("asd"), 200