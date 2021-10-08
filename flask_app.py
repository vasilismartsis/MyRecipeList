from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response, Blueprint
from flask_sqlalchemy import SQLAlchemy
import re

from account import account
from addRecipe import addRecipe
from database import *

app.register_blueprint(account, url_prefix="/account")
app.register_blueprint(addRecipe, url_prefix="/addRecipe")

app.secret_key = "mySecretKey"

# routes
@app.route("/")
def index():
    return render_template("index.html")


# print(db.session.query(users.email).all()[1:])
# print(users.query.all())
# print(users.query.with_entities(users.email).all())


@app.route("/getDbIngredients", methods=["POST", "GET"])
def getDbIngredients():
    if request.method == "POST":
        r = request.get_json()
    else:
        r = format(request.args.get("ingredients"))

    ingredientsClientList = r.lower().split(",")

    recipesDbList = []

    for i in range(0, len(ingredientsClientList)):
        ingredientsClientList[i] = re.sub('^ ', '', ingredientsClientList[i])
        ingredientsClientList[i] = re.sub(' $', '', ingredientsClientList[i])
        if recipes.query.filter(recipes.ingredients.like("%" + ingredientsClientList[i] + "%")).all() not in recipesDbList:
            recipesDbList += recipes.query.filter(
                recipes.ingredients.like("%" + ingredientsClientList[i] + "%")).all()

    recipesDbList = list(dict.fromkeys(recipesDbList))  # remove duplicates

    recipesList = recipesSchema(many=True).dump(recipesDbList)

    for i in range(0, len(recipesList)):
        ingredientsList = recipesList[i]["ingredients"].split(",")

        usedIngredients = []
        unusedIngredients = []
        missedIngredients = []

        for ingredientClient in ingredientsClientList:
            if(ingredientClient in ingredientsList):
                usedIngredients.append({"name": ingredientClient})
                ingredientsList.remove(ingredientClient)
            else:
                unusedIngredients.append({"name": ingredientClient})

        for ingredient in ingredientsList:
            missedIngredients.append({"name": ingredient})

        recipesList[i]["usedIngredients"] = usedIngredients
        recipesList[i]["unusedIngredients"] = unusedIngredients
        recipesList[i]["missedIngredients"] = missedIngredients

    bubbleSort(recipesList)

    return make_response(jsonify(recipesList), 200)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if len(arr[j]["missedIngredients"]) > len(arr[j+1]["missedIngredients"]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
