from models.adventurer import Adventurer
from db.run_sql import run_sql

from models.lesson import Lesson
from models.enrolment import Enrolment

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

#UPDATE
##update adventurer

#DELETE
##delete all
def delete_all():
    sql = "DELETE FROM adventurers"
    run_sql(sql)

#delete adventurer(id)