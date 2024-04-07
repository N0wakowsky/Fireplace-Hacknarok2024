from flask import Flask, redirect, render_template
from flask_login import current_user
from flask_socketio import SocketIO

from app.backend.fireplaces import fireplace_manager
from app.blueprints.api import api, socket
from app.blueprints.auth import auth, login_manager
from app.models import User, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/database.db"
app.config["SECRET_KEY"] = "MASZIN"

db.init_app(app)
login_manager.init_app(app)
socket.init_app(app)


with app.app_context():
    db.create_all()

app.register_blueprint(api)
app.register_blueprint(auth)


@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("join.html", username=current_user.username)
    return redirect("/auth/login")


@app.route("/fireplace/<string:code>", methods=["GET"])
def fireplace(code: int):
    fireplace = fireplace_manager.get_fireplace(code)

    if not fireplace:
        return redirect("/")

    if current_user.id == fireplace.host_id:
        return render_template(
            "fireplacemaster.html",
            title=fireplace.title,
            code=fireplace.code,
            username=current_user.username,
        )

    if not current_user.id in fireplace.get_guest_ids():
        user = User.query.get_or_404(current_user.id)
        user.visits += 1
        user.points += 5
        user.active = True
        db.session.commit()
        fireplace.add_guest(current_user.id)
        socket.emit("update")

    host = User.query.get_or_404(fireplace.host_id)

    return render_template(
        "fireplace.html",
        title=fireplace.title,
        username=current_user.username,
        host_username=host.username,
    )


@app.route("/ranking", methods=["GET"])
def ranking():
    return render_template(
        "ranking.html",
        rank_list=User.query.order_by(User.points.desc()).all(),
        username=current_user.username,
    )
