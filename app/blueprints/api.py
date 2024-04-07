from flask import Blueprint, jsonify, redirect, request
from flask_login import current_user, login_required
from flask_socketio import SocketIO

from app.backend.fireplaces import fireplace_manager
from app.models import User, db

api = Blueprint("api", __name__, url_prefix="/api")

socket = SocketIO()


@socket.on("host_leave")
def handle_host_leave(code):
    print("host leave", code)
    socket.emit("fireplace_closed", code)
    fireplace_manager.remove_fireplace(code)


@api.route("/fireplace/<string:code>/leave", methods=["GET"])
@login_required
def api_fireplace_leave(code: str):
    fireplace = fireplace_manager.get_fireplace(code)

    if not fireplace:
        return f"No fireplace with code {code}"

    if current_user.id == fireplace.host_id:
        fireplace_manager.remove_fireplace(code)
        socket.emit("fireplace_closed", code)
    else:
        fireplace.remove_guest(current_user.id)
        socket.emit("update")

    return redirect(f"/")


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
        return redirect("/")

    names = User.query.filter(User.id.in_(fireplace.guests)).all()
    json_data = [[item.username, item.active] for item in names]

    return jsonify(json_data)


@api.route("/user/out", methods=["GET"])
@login_required
def user_out():
    user = User.query.get_or_404(current_user.id)
    if user.points > 0:
        user.points -= 1
    user.active = False
    db.session.commit()

    socket.emit("update")

    return "", 200


@api.route("/user/in", methods=["GET"])
@login_required
def user_in():
    user = User.query.get_or_404(current_user.id)
    user.active = True
    db.session.commit()

    socket.emit("update")

    return "", 200
