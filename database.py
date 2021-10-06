from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyRecipeList.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    link = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    ingredients = db.Column(db.String(200))

    def __init__(self, title, image, link, description, ingredients):
        self.title = title
        self.image = image
        self.link = link
        self.description = description
        self.ingredients = ingredients


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = users


class recipesSchema(ma.ModelSchema):
    class Meta:
        model = recipes
