class Instructor():
    """
    Represents an instructor object
    Attributes:
        first_name (str): instructor's first name
        last_name (str): instructor's last name
        slack (str): instructor's slack handle
        cohort (str): instructor's cohort
        specialty (str): instructor's specialty
    """

    def __init__(self, first, last, slack, cohort, specialty):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)
