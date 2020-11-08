from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    order = db.relationship("Order")

    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def password_valid(self, password: str):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    meals = db.relationship("Meal")


class Meal(db.Model):
    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    category = db.relationship("Category")
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    meals = db.Column(db.String, nullable=False)

    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
