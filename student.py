class Student():
    """
    Represents a student object
    Attributes:
        first_name (str): student's first name
        last_name (str): student's last name
        slack (str): student's slack handle
        cohort (str): student's cohort
        exercises (list): collection of exercises
    """

    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
