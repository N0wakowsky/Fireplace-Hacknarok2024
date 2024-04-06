from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(40)])
    password = PasswordField("Password", validators=[DataRequired(), Length(40)])
    submit = SubmitField("Login")
