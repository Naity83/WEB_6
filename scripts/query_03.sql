SELECT g.group_name, ROUND(AVG(gr.grade), 2) AS average_grade
        FROM grades gr
        JOIN students s ON gr.student_id = s.id
        JOIN groups g ON s.group_id = g.id
        JOIN subjects subj ON gr.subject_id = subj.id
        WHERE subj.subject = 'Фізика'
        GROUP BY g.group_name;