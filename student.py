from nssperson import NSSPerson


class Student(NSSPerson):
    """
    Represents a student object
    Inherits from NSS Person:
        first_name (str): student's first name
        last_name (str): student's last name
        slack (str): student's slack handle
        cohort (str): student's cohort
    Unique Attributes:
        exercises (list): collection of exercises
    Methods:
        add_exercises: adds exercise object to list
    """

    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
