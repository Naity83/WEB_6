SELECT t.fullname, ROUND(AVG(g.grade), 2) AS average_grade
        FROM teachers t
        JOIN subjects s ON t.id = s.teacher_id
        JOIN grades g ON s.id = g.subject_id
        GROUP BY t.fullname
        HAVING t.fullname = 'Сидоров Сидор';