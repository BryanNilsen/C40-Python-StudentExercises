from nssperson import NSSPerson


class Instructor(NSSPerson):
    """
    Represents an instructor object
    Inherits from NSS Person:
        first_name (str): instructor's first name
        last_name (str): instructor's last name
        slack (str): instructor's slack handle
        cohort (str): instructor's cohort
    Unique Attributes:
        specialty: instructor's primary programming language
    Methods:
        assign_exercises: assigns exercise object to student exercises list
    """

    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first, last, slack, cohort)
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}- {self.cohort}'
