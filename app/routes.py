from flask import Flask, redirect, render_template, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.backend.fireplaces import fireplace_manager
from app.forms import LoginForm
from app.models import User, db

app = Flask(__name__)
login_manager = LoginManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/database.db"
app.config["SECRET_KEY"] = "MASZIN"

db.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return f"{User.query.all()[0].username}, {User.query.all()[0].password}"


@app.route("/join")
def join():
    return render_template("join.html")


@app.route("/test")
@login_required
def test():
    return f"{current_user.username} {current_user.password}"


@app.route("/user/register", methods=["GET", "POST"])
def register():
    if request.method == "get":
        return render_template("register.html")

    elif request.method == "post":
        user = User(
            username=request.form.get("username"),
            password=generate_password_hash(request.form.get("password")),
        )
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

        return redirect("/test")
    else:
        return render_template("register.html")


@app.route("/user/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", username=[1, 2, 3])

    elif request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user:
            if check_password_hash(user.password, request.form.get("password")):
                login_user(user, remember=True)

        return redirect("/test")


@app.route("/user/logout", methods=["GET"])
@login_required
def logout():
    logout_user()

    return redirect("/user/login")


@app.route("/fireplace/create", methods=["POST"])
@login_required
def fireplace_create():
    code = fireplace_manager.add_fireplace(current_user.id, request.form.get("title"))

    return redirect(f"/fireplace/{code}")


@app.route("/fireplace/<string:code>", methods=["GET"])
def fireplace(code: int):
    if not fireplace_manager.get_fireplace(code):
        return f"no fireplace with code {code}"

    return render_template("fireplace")


@app.route("/ranking", methods=["GET"])
def ranking():
    return render_template("ranking.html")
