from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.adventurer import Adventurer
import repositories.adventurer_repository as adventurer_repository

adventurers_blueprint = Blueprint("adventurers", __name__)

@adventurers_blueprint.route("/adventurers")
def adventurers():
    adventurers = adventurer_repository.select_all()
    return render_template("adventurers/index.html", adventurers=adventurers)