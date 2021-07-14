from db.run_sql import run_sql
from models.adventurer import Adventurer
from models.lesson import Lesson

##CREATE
##save adventurer
def save(adventurer):
    sql = "INSERT INTO adventurers (first_name, last_name, adventurer_class) VALUES (%s, %s, %s) RETURNING id"
    values = [adventurer.first_name, adventurer.last_name, adventurer.adventurer_class]
    results = run_sql(sql, values)
    adventurer.id = results[0]['id']
    return adventurer

##READ
##select all adventurers
def select_all():
    adventurers = []

    sql = "SELECT * FROM adventurers"
    results = run_sql(sql)
    for row in results:
        adventurer = Adventurer(row['first_name'], row['last_name'], row['adventurer_class'], row['id'])
        adventurers.append(adventurer)
    return adventurers

##select adventurer(id)
def select(id):
    adventurer = None
    sql = "SELECT * FROM adventurers WHERE id = %s"
    values=[id]
    result = run_sql(sql, values)[0]

    if result != None:
        adventurer = Adventurer(result['first_name'], result['last_name'], result['adventurer_class'], result['id'])
    return adventurer

##return all lessons that an adventurer has enrolled in
def lessons(adventurer):
    lessons = []

    sql = "SELECT lessons.* FROM lessons INNER JOIN enrolments ON enrolments.lesson_id = lessons.id WHERE adventurer_id = %s"
    values = [adventurer.id]
    results = run_sql(sql, values)

    for row in results:
        lesson = Lesson(row['lesson_name'], row['recommended_for'], row['lesson_description'], row['id'])
        lessons.append(lesson)
    return lessons

#UPDATE
##update adventurer
def update_adventurer(adventurer):
    sql = "UPDATE adventurers SET (first_name, last_name, adventurer_class) = (%s, %s, %s) WHERE id = %s"
    values = [adventurer.first_name, adventurer.last_name, adventurer.adventurer_class, adventurer.id]
    run_sql(sql, values)
    return adventurer

#DELETE
##delete all
def delete_all():
    sql = "DELETE FROM adventurers"
    run_sql(sql)

# delete adventurer(id)
def delete_adventurer(id):   
    sql = "DELETE FROM adventurers WHERE id = %s"
    values = [id]
    run_sql(sql, values)