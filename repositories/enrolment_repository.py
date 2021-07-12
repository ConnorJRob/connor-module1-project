from db.run_sql import run_sql
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository

##CREATE
##save enrolment
def save(enrolment):
    sql = "INSERT INTO enrolments (adventurer_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [enrolment.adventurer.id, enrolment.lesson.id]
    results = run_sql(sql, values)
    enrolment.id = results[0]['id']
    return enrolment

##READ
##select all enrolments
def select_all():
    enrolments = []

    sql = "SELECT * FROM enrolments"
    results = run_sql(sql)

    for row in results:
        adventurer = adventurer_repository.select(row['adventurer_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        enrolment = Enrolment(adventurer, lesson, row['id'])
        enrolments.append(enrolment)
    return enrolments

##return the lesson associated with a specific enrolment
##return the adventurer associated with a specific enrolment

#DELETE
##delete all
#delete enrolment(id)