from db.run_sql import run_sql
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

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

#UPDATE
##update lesson

#DELETE
##delete all
#delete lesson(id)

# CREATE TABLE lessons (
#     id SERIAL PRIMARY KEY,
#     lesson_name VARCHAR(255),
#     recommended_for VARCHAR(255),
#     lesson_description TEXT
# );
