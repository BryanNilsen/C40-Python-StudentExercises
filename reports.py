import sqlite3


class Student():

    def __init__(self, id, first, last, handle, cohort):
        self.id = id
        self.first_name = first
        self.last_name = last
        self.slackhandle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


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

            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')


reports = StudentExerciseReports()
reports.all_students()
