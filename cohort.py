class Cohort():
    """
    Represents a cohort object
    Attributes:
        name (str): name of cohort
        students (list): collection of students in cohort
        instructors (list): collection of instructors in cohort
    """

    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []

    # def add_student(self, student_dict):
    #     self.students.add(student_dict)

    # def add_instructor(self, instructor_dict):
    #     self.instructors.add(instructor_dict)
