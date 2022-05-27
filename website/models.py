from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Calorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.Date)
    breakfast_green = db.Column(db.Integer)
    lunch_green = db.Column(db.Integer)
    dinner_green = db.Column(db.Integer)
    snack_green = db.Column(db.Integer)
    breakfast_yellow = db.Column(db.Integer)
    lunch_yellow = db.Column(db.Integer)
    dinner_yellow = db.Column(db.Integer)
    snack_yellow = db.Column(db.Integer)
    breakfast_red = db.Column(db.Integer)
    lunch_red = db.Column(db.Integer)
    dinner_red = db.Column(db.Integer)
    snack_red = db.Column(db.Integer)
    # data = db.Column(db.String(10000))
    date_time = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    calories = db.relationship('Calorie')
