from models.lesson import Lesson


class Enrolment:
    def __init__(self, adventurer, lesson, id = None):
        self.adventurer = adventurer
        self.lesson = lesson
        self.id = id