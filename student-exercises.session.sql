DROP TABLE cohorts;
DROP TABLE students;


CREATE TABLE cohorts
(
    cohort_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students
(
    student_id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slackhandle TEXT NOT NULL UNIQUE,
    cohort_id INTEGER NOT NULL,
    FOREIGN KEY(cohort_id) REFERENCES Cohort(cohort_id)
);