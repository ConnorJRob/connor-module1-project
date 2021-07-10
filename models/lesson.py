class Lesson:
    def __init__(self, lesson_name, recommended_for, description, id = None):
        self.lesson_name = lesson_name
        self.recommended_for = recommended_for
        self.description = description
        self.id = id