import pdb
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository
import repositories.enrolment_repository as enrolment_repository

# adventurer_1 = Adventurer("Zimazz", "Greenwind", "Wizard")
# adventurer_repository.save(adventurer_1)

adventurer_2 = Adventurer("Eldak", "Belzor", "Ranger")
adventurer_repository.save(adventurer_2)

print(adventurer_repository.select_all())

pdb.set_trace()