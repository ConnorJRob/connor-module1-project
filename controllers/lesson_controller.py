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
    lesson_name = request.form['lesson-name']
    recommended_for = request.form['recommended_for']
    lesson_description = request.form['lesson_description']
    lesson = Lesson(lesson_name, recommended_for, lesson_description)
    lesson_repository.save(lesson)
    return redirect("/lessons")