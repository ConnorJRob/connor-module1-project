from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.enrolment import Enrolment
import repositories.enrolment_repository as enrolment_repository
import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository

enrolments_blueprint = Blueprint("enrolments", __name__)

# NEW
# GET '/enrolments
@enrolments_blueprint.route("/enrolments")
def new_enrolment():
    lessons = lesson_repository.select_all()
    adventurers = adventurer_repository.select_all()
    return render_template("enrolments/new.html", lessons=lessons, adventurers=adventurers)


# CREATE
# POST '/enrolments/new
@enrolments_blueprint.route("/enrolments/new", methods=['POST'])
def create_enrolment():
    adventurer_id = request.form['adventurer']
    adventurer = adventurer_repository.select(adventurer_id)
    lesson_id = request.form['lesson']
    lesson = lesson_repository.select(lesson_id)
    enrolment = Enrolment(adventurer, lesson)
    enrolment_repository.save(enrolment)
    return redirect("/")