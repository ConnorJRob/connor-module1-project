from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)

# GET
@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons=lessons)

# GET /lessons/id
@lessons_blueprint.route("/lessons/<id>")
def show(id):
    lesson = lesson_repository.select(id)
    adventurers = lesson_repository.adventurers(lesson)
    return render_template("lessons/show.html", lesson=lesson, adventurers=adventurers)

# NEW
# GET '/lessons/new
@lessons_blueprint.route("/lessons/new")
def new_lesson():
    return render_template("lessons/new.html")

# CREATE
# POST '/lessons'
@lessons_blueprint.route("/lessons", methods=['POST'])
def create_lesson():
    lesson_name = request.form['lesson_name']
    recommended_for = request.form['recommended_for']
    lesson_description = request.form['lesson_description']
    lesson = Lesson(lesson_name, recommended_for, lesson_description)
    saved_lesson = lesson_repository.save(lesson)
    return_location="/lessons/"+str(saved_lesson.id)
    return redirect(return_location)

# EDIT
# GET '/adventurers/<id>/edit'
@lessons_blueprint.route("/lessons/<id>/edit")
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    adventurer_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    return render_template("lessons/edit.html", lesson=lesson, adventurer_classes=adventurer_classes)

# # UPDATE
# # PUT '/adventurers/<id>'
@lessons_blueprint.route("/lessons/<id>", methods=['POST'])
def update_lesson(id):
    lesson = lesson_repository.select(id)
    lesson.lesson_name = request.form['lesson_name']
    lesson.recommended_for = request.form['recommended_for']
    lesson.lesson_description = request.form['lesson_description']
    lesson = Lesson(lesson.lesson_name, lesson.recommended_for, lesson.lesson_description, id)
    updated_lesson = lesson_repository.update_lesson(lesson)
    return_location = "/lessons/"+str(updated_lesson.id)
    return redirect(return_location)


# DELETE
# PUT '/adventurers/<id>/delete'
@lessons_blueprint.route("/lessons/<id>/delete", methods=['POST'])
def delete_lesson(id):
    lesson_repository.delete_lesson(id)
    return redirect("/lessons")