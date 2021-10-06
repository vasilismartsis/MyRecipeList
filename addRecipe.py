from flask import Flask, Blueprint, render_template, request, make_response, jsonify, json, session
from database import *

addRecipe = Blueprint("addRecipe", __name__, static_folder="static",
                      template_folder="templates")


@addRecipe.route("/", methods=["POST", "GET"])
def addRecipePage():
    if "username" in session:
        if request.method == "POST":
            title = request.form["title"]
            image = request.form["image"]
            link = request.form["link"]
            description = request.form["description"]
            ingredients = request.form["ingredients"].lower()

            foundRecipy = recipes.query.filter_by(title=title).first()
            if foundRecipy:
                return render_template("index.html", content="addRecipe", status="alreadyExists")
            else:
                recipy = recipes(title, image, link, description, ingredients)
                db.session.add(recipy)
                db.session.commit()
                return render_template("index.html", content="addRecipe", status="success")
        else:
            return render_template("index.html", content="addRecipe")
    else:
        return render_template("index.html", content="loginFirst")
