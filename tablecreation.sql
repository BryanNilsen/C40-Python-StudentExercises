DELETE FROM cohorts;
DELETE FROM students;
DELETE FROM instructors;
DELETE FROM exercises;
DELETE FROM student_exercises;

DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS student_exercises;
DROP TABLE IF EXISTS exercises;

CREATE TABLE cohorts (
    cohort_id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slackhandle TEXT NOT NULL UNIQUE,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY (cohort_id) REFERENCES Cohort (cohort_id)
);

CREATE TABLE instructors (
    instructor_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slackhandle TEXT NOT NULL UNIQUE,
    specialty TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY (cohort_id) REFERENCES Cohort (cohort_id)
);

CREATE TABLE exercises (
    exercise_id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    language TEXT NOT NULL
);

CREATE TABLE student_exercises (
    student_exercise_id INTEGER NOT NULL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student (student_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercises (exercise_id)
);

INSERT INTO cohorts ("name")
VALUES ("Cohort 28");

INSERT INTO cohorts ("name")
VALUES ("Cohort 32");

INSERT INTO cohorts ("name")
VALUES ("Cohort 34");

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Sebastian", "Civarolo", "SebastianCiv", 1);

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Robby", "Hecht", "RobbyHecht", 1);

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Dan", "Storm", "DanceStorm", 2);

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Eliot", "Clarke", "EliotClarke", 2);

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Curtis", "Crutchfield", "CurtisCrutchfield",  3);

INSERT INTO students ("first_name", "last_name", "slackhandle", "cohort_id")
VALUES ("Jacquelyn", "McCray", "JacquelynMcCray", 3);

INSERT INTO instructors ("first_name", "last_name", "slackhandle", "specialty", "cohort_id")
VALUES ("Steve", "Brownlee", "Coach", "Javascript", 2);

INSERT INTO instructors ("first_name", "last_name", "slackhandle", "specialty", "cohort_id")
VALUES ("Joe", "Shepherd", "Joes", "Python", 1);

INSERT INTO instructors ("first_name", "last_name", "slackhandle", "specialty", "cohort_id")
VALUES ("Jisie", "David", "Jisie", "C#", 3);

INSERT INTO exercises ("name", "language")
VALUES ("ChickenMonkey", "Javascript");

INSERT INTO exercises ("name", "language")
VALUES ("Kennel", "React");

INSERT INTO exercises ("name", "language")
VALUES ("KandyKorner", "React");

INSERT INTO exercises ("name", "language")
VALUES ("Flexbox Froggy", "CSS");

INSERT INTO exercises ("name", "language")
VALUES ("Keahua", "Python");

INSERT INTO exercises ("name", "language")
VALUES ("Trestlebridge", "C#");

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (1, 1);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (1, 4);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (2, 2);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (2,3);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (3, 1);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (3, 4);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (4, 1);

INSERT INTO student_exercises ("student_id", "exercise_id")
VALUES (4, 3);