import pdb
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository
import repositories.enrolment_repository as enrolment_repository


# adventurer_repository.delete_all()

# adventurer_1 = Adventurer("Zimazz", "Greenwind", "Wizard")
# adventurer_repository.save(adventurer_1)

# adventurer_2 = Adventurer("Eldak", "Belzor", "Ranger")
# adventurer_repository.save(adventurer_2)

# adventurer_3 = Adventurer("Grog", "Strongjaw", "Barbarian")
# adventurer_repository.save(adventurer_3)

# adventurers = adventurer_repository.select_all()

# adventurer = adventurer_repository.select(1)

# adventurer_repository.delete_adventurer(2)

adventurers = adventurer_repository.select_all()

pdb.set_trace()