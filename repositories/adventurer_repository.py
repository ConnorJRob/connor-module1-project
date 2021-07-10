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

#UPDATE
##update adventurer

#DELETE
##delete all
#delete adventurer(id)