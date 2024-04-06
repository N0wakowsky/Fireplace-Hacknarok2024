from flask import Blueprint, redirect, render_template, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User, db

auth = Blueprint("auth", __name__, url_prefix="/auth")

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        user = User(
            username=request.form.get("username"),
            password=generate_password_hash(request.form.get("password")),
        )
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

        return redirect("/")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user:
            if check_password_hash(user.password, request.form.get("password")):
                login_user(user, remember=True)

        return redirect("/")


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()

    return redirect("/user/login")
