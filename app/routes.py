from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash, generate_password_hash

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
    return f"{User.query.all()[0].username}, {User.query.all()[0].password_hash}"


@app.route("/join")
def join():
    return render_template("join.html")


@app.route("/test")
@login_required
def test():
    return f"{current_user.username} {current_user.password_hash}"


@app.route("/user/register", methods=["GET", "POST"])
def register():
    user = User(
        username=request.args.get("user"),
        password_hash=generate_password_hash(request.args.get("pass")),
    )
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)
    flash("Konto zostało utworzone", "success")

    return redirect("/")


@app.route("/user/login", methods=["GET", "POST"])
def login():
    user = User.query.filter_by(username=request.args.get("user")).first()
    if user:
        if check_password_hash(user.password_hash, request.args.get("pass")):
            login_user(user, remember=True)

    return redirect("/test")


@app.route("/user/logout", methods=["GET"])
@login_required
def logout():
    logout_user()

    return redirect(url_for("/user/login"))
