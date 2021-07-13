from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.adventurer import Adventurer
import repositories.adventurer_repository as adventurer_repository

adventurers_blueprint = Blueprint("adventurers", __name__)

# SHOW ALL
# GET '/adventurers
@adventurers_blueprint.route("/adventurers")
def adventurers():
    adventurers = adventurer_repository.select_all()
    return render_template("adventurers/index.html", adventurers=adventurers)

# SHOW 
# GET '/adventurers/id
@adventurers_blueprint.route("/adventurers/<id>")
def show(id):
    adventurer = adventurer_repository.select(id)
    lessons = adventurer_repository.lessons(adventurer)
    return render_template("adventurers/show.html", adventurer=adventurer, lessons=lessons)

# NEW
# GET '/lessons/new
@adventurers_blueprint.route("/adventurers/new")
def new_adventurer():
    return render_template("adventurers/new.html")

# CREATE
# POST '/adventurers'
@adventurers_blueprint.route("/adventurers", methods=['POST'])
def create_adventurer():
    first_name = request.form['adventurer-first-name']
    last_name = request.form['adventurer-last-name']
    adventurer_class = request.form['adventurer-class']
    adventurer = Adventurer(first_name, last_name, adventurer_class)
    adventurer_repository.save(adventurer)
    return redirect("/adventurers")

# EDIT
# GET '/adventurers/<id>/edit'
@adventurers_blueprint.route("/adventurers/<id>/edit")
def edit_adventurer(id):
    adventurer = adventurer_repository.select(id)
    adventurer_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    return render_template("adventurers/edit.html", adventurer=adventurer, adventurer_classes=adventurer_classes)

# UPDATE
# PUT '/adventurers/<id>'
@adventurers_blueprint.route("/adventurers/<id>", methods=['POST'])
def update_adventurer(id):
    adventurer = adventurer_repository.select(id)
    adventurer.first_name = request.form['adventurer-first-name']
    adventurer.last_name = request.form['adventurer-last-name']
    adventurer.adventurer_class = request.form['adventurer-class']
    adventurer_repository.update_adventurer(adventurer)
    return redirect("/adventurers")
