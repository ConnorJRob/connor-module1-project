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

##select enrolment by id (mostly for testing purposes)
def select(id):
    enrolment = None
    sql = "SELECT * FROM enrolments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        adventurer = adventurer_repository.select(result['adventurer_id'])
        lesson = lesson_repository.select(result['lesson_id'])
        enrolment = Enrolment(adventurer, lesson, result['id'])
    return enrolment

##return the lesson associated with a specific enrolment
def lesson(enrolment):
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [enrolment.lesson.id]
    results = run_sql(sql, values)[0]
    lesson = Lesson(results['lesson_name'], results['recommended_for'], results['lesson_description'])
    return lesson

##return the adventurer associated with a specific enrolment
def adventurer(enrolment):
    sql = "SELECT * FROM adventurers WHERE id = %s"
    values = [enrolment.adventurer.id]
    results = run_sql(sql, values)[0]
    adventurer = Adventurer(results['first_name'], results['last_name'], results['adventurer_class'], results['id'])
    return adventurer

#DELETE
##delete all
def delete_all():
    sql = "DELETE FROM enrolments"
    run_sql(sql)

#delete enrolment(id)
def delete(id):
    sql = "DELETE FROM enrolments WHERE id = %s"
    values = [id]
    run_sql(sql, values)