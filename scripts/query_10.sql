SELECT DISTINCT sj.subject AS course_name
        FROM students s
        JOIN grades g ON s.id = g.student_id
        JOIN subjects sj ON g.subject_id = sj.id
        JOIN teachers t ON sj.teacher_id = t.id
        WHERE s.fullname = 'Зорян Ященко'
        AND t.fullname = 'Іванов Іван';