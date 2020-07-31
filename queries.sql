SELECT *
FROM cohorts;

SELECT *
FROM students;

select s.student_id,
    s.first_name,
    s.last_name,
    s.slackhandle,
    s.cohort_id,
    c.name
from Students s
join Cohorts c on s.cohort_id = c.cohort_id
order by s.cohort_id

select i.instructor_id,
    i.first_name,
    i.last_name,
    i.slackhandle,
    i.cohort_id,
    c.name
from Instructors i
join Cohorts c on i.cohort_id = c.cohort_id
