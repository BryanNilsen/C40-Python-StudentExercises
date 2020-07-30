DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
CREATE TABLE cohorts
(
    cohort_id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE students
(
    student_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slackhandle TEXT NOT NULL UNIQUE,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY (cohort_id) REFERENCES Cohort (cohort_id)
);
CREATE TABLE instructors
(
    instructor_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    slackhandle TEXT NOT NULL UNIQUE,
    specialty TEXT NOT NULL,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY (cohort_id) REFERENCES Cohort (cohort_id)
);