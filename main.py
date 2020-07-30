from exercise import Exercise
from instructor import Instructor
from student import Student
from cohort import Cohort

chickenmonkey = Exercise("ChickenMonkey", "Javascript")
kennel = Exercise("Kennel", "React")
kandykorner = Exercise("KandyKorner", "React")
flexboxfroggy = Exercise("Flexbox Froggy", "CSS")

c32 = Cohort("Cohort 32")
c28 = Cohort("Cohort 28")
c34 = Cohort("Cohort 34")

scivarolo = Student("Sebastian", "Civarolo", "SebastianCiv", "c28")
rhecht = Student("Robby", "Hecht", "RobbyHecht", c28)
dstorm = Student("Dan", "Storm", "DanceStorm", c32)
eclarke = Student("Eliot", "Clarke", "EliotClarke", c32)
ccrutchfield = Student("Curtis", "Crutchfield", "CurtisCrutchfield", c32)
jmccray = Student("Jacquelyn", "McCray", "JacquelynMcCray", c34)

sbrownlee = Instructor("Steve", "Brownlee", "Coach", c32, "Javascript")
jshep = Instructor("Joe", "Shepherd", "Joes", c28, "Python")
jdavid = Instructor("Jisie", "David", "Jisie", c34, "C#")


# have instructors assign exercises
jshep.assign_exercise(rhecht, chickenmonkey)
jshep.assign_exercise(rhecht, kennel)
jshep.assign_exercise(scivarolo, chickenmonkey)
jshep.assign_exercise(scivarolo, kandykorner)
sbrownlee.assign_exercise(dstorm, flexboxfroggy)
sbrownlee.assign_exercise(dstorm, kandykorner)
sbrownlee.assign_exercise(eclarke, kennel)
sbrownlee.assign_exercise(eclarke, flexboxfroggy)
jdavid.assign_exercise(ccrutchfield, chickenmonkey)
jdavid.assign_exercise(ccrutchfield, flexboxfroggy)
jdavid.assign_exercise(jmccray, kennel)
jdavid.assign_exercise(jmccray, kandykorner)

students = list()
students.extend([scivarolo, rhecht, dstorm, eclarke, jmccray, ccrutchfield])

exercises = list()
exercises.extend([chickenmonkey, kandykorner, kennel, flexboxfroggy])


def student_exercise_report():
    for student in students:
        student_exercises = []
        for exercise in student.exercises:
            student_exercises.append(exercise.name)
        print(f"{student.first_name} is working on {' and '.join(student_exercises)}.")


student_exercise_report()
