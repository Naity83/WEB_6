SELECT ROUND(AVG(g.grade), 2) AS average_grade
        FROM grades g
        JOIN subjects sj ON g.subject_id = sj.id
        JOIN teachers t ON sj.teacher_id = t.id
        JOIN students s ON g.student_id = s.id
        WHERE t.fullname = 'Іванов Іван'
        AND s.fullname = 'Зорян Ященко';