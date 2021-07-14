import pdb
from models.adventurer import Adventurer
from models.lesson import Lesson
from models.enrolment import Enrolment

import repositories.adventurer_repository as adventurer_repository
import repositories.lesson_repository as lesson_repository
import repositories.enrolment_repository as enrolment_repository


adventurer_1 = Adventurer("Zimazz", "Greenwind", "Wizard")
adventurer_repository.save(adventurer_1)

adventurer_2 = Adventurer("Eldak", "Belzor", "Ranger")
adventurer_repository.save(adventurer_2)

adventurer_3 = Adventurer("Grog", "Strongjaw", "Barbarian")
adventurer_repository.save(adventurer_3)

adventurer_4 = Adventurer("Scanlan", "Shorthalt", "Bard")
adventurer_repository.save(adventurer_4)

adventurer_5 = Adventurer("Pike", "Trickfoot", "Cleric")
adventurer_repository.save(adventurer_5)

adventurer_6 = Adventurer("Jester", "Lavore", "Cleric")
adventurer_repository.save(adventurer_6)

adventurer_7 = Adventurer("Gregory", "Keenheart", "Paladin")
adventurer_repository.save(adventurer_7)

adventurer_8 = Adventurer("Craydur", "Rath", "Fighter")
adventurer_repository.save(adventurer_8)


lesson_1 = Lesson("Orcish for Beginners", "Wizard", "A beginner's class in speaking Orcish, making sure to avoid getting killed for saying something about someone's mother by accident")
lesson_repository.save(lesson_1)

lesson_2 = Lesson("How and when to use Fireball", "Wizard", "Not all the time.")
lesson_repository.save(lesson_2)

lesson_3 = Lesson("When is it a mimic?", "Bard", "Assume always.")
lesson_repository.save(lesson_3)

lesson_3 = Lesson("Initivate, what is it and what does it matter?", "Cleric", "If you're not fast, you're last")
lesson_repository.save(lesson_3)




# pdb.set_trace()