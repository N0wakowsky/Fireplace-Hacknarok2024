from flask import Blueprint, jsonify, redirect, request
from flask_login import current_user, login_required

from app.backend.fireplaces import fireplace_manager
from app.models import User

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/fireplace/create", methods=["POST"])
@login_required
def api_fireplace_create():
    code = fireplace_manager.add_fireplace(current_user.id, request.form.get("title"))

    return redirect(f"/fireplace/{code}")


@api.route("/fireplace/<string:code>/get_users", methods=["GET"])
@login_required
def api_fireplace_get_users(code: int):

    fireplace = fireplace_manager.get_fireplace(code)

    if not fireplace:
        return f"No fireplace with code {code}"

    names = User.query.filter(User.id.in_(fireplace.guests)).all()

    return jsonify(names)
