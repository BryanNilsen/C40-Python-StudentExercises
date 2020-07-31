import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/bryannilsen/Workspace/C40/Python/StudentExercises/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select s.student_id,
                    s.first_name,
                    s.last_name,
                    s.slackhandle,
                    s.cohort_id,
                    c.name
                from Students s
                join Cohorts c on s.cohort_id = c.cohort_id
                order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            # traditional loop:
            # for student in all_students:
            #     print(student)
            print("Students")
            print("==========")
            # comprehension:
            [print(s) for s in all_students]
            print("")

    def all_cohorts(self):
        """Retrieve all cohorts with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select c.cohort_id, c.name
                from Cohorts c
                order by c.cohort_id
            """)

            all_cohorts = db_cursor.fetchall()
            print("Cohorts")
            print("==========")
            # comprehension:
            [print(c) for c in all_cohorts]
            print("")

    def all_exercises(self):
        """Retrieve all exercises with the name and language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.name, e.language
                from Exercises e
            """)

            title = f"All Exercises"
            all_exercises = db_cursor.fetchall()
            print(title)
            print("=" * len(title))
            # comprehension:
            [print(e) for e in all_exercises]
            print("")

    def all_exercises_by_language(self, language):
        """Retrieve all exercises with the name and language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1])

            lang = (f"%{language}%",)
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.name, e.language
                from Exercises e
                where e.language LIKE ?
            """, lang)

            title = f"Exercises - searched: '{language}'"
            all_exercises = db_cursor.fetchall()
            print(title)
            print("=" * len(title))
            # comprehension:
            [print(e) for e in all_exercises]
            print("")

    def all_instructors_with_cohort(self):
        """Retrieve all instructors with the their cohort"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5], row[6])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.instructor_id,
                i.first_name,
                i.last_name,
                i.slackhandle,
                i.cohort_id,
                c.name,
                i.specialty
            from Instructors i
            join Cohorts c on i.cohort_id = c.cohort_id
            order by i.cohort_id
            """)

            all_instructors = db_cursor.fetchall()
            print("Instructors")
            print("=========")
            # comprehension:
            [print(i) for i in all_instructors]
            print("")


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_exercises_by_language("Javascript")
reports.all_exercises_by_language("Python")
reports.all_exercises_by_language("C#")

reports.all_instructors_with_cohort()
