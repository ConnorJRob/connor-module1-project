from repositories.enrolment_repository import adventurer
from db.run_sql import run_sql
from models.adventurer import Adventurer
from models.lesson import Lesson

##CREATE
##save lesson
def save(lesson):
    sql = "INSERT INTO lessons (lesson_name, recommended_for, lesson_description) VALUES (%s, %s, %s) RETURNING id"
    values = [lesson.lesson_name, lesson.recommended_for, lesson.lesson_description]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

##READ
##select all lessons
def select_all():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)
    for row in results:
        lesson = Lesson(row['lesson_name'], row['recommended_for'], row['lesson_description'], row['id'])
        lessons.append(lesson)
    return lessons

##select lesson(id)
def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        lesson = Lesson(result['lesson_name'], result['recommended_for'], result['lesson_description'], result['id'])
    return lesson

##return all adventurers that have enrolled in a specific lesson
def adventurers(lesson):
    adventurers = []

    sql = "SELECT adventurers.* FROM adventurers INNER JOIN enrolments ON enrolments.adventurer_id = adventurers.id WHERE lesson_id = %s"
    values = [lesson.id]
    results = run_sql(sql, values)

    for row in results:
        adventurer = Adventurer(row['first_name'], row['last_name'], row['adventurer_class'], row['id'])
        adventurers.append(adventurer)
    return adventurers


#UPDATE
##update lesson
def update_lesson(lesson):
    sql = "UPDATE lessons SET (lesson_name, recommended_for, lesson_description) = (%s, %s, %s) WHERE id = %s"
    values = [lesson.lesson_name, lesson.recommended_for, lesson.lesson_description, lesson.id]
    run_sql(sql, values)


#DELETE
##delete all
def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)

#delete lesson(id)

def delete_lesson(id):   
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)
