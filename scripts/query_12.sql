SELECT s.fullname AS student_name, g.grade
        FROM grades g
        JOIN students s ON g.student_id = s.id
        JOIN subjects sj ON g.subject_id = sj.id
        JOIN teachers t ON sj.teacher_id = t.id
        JOIN groups gr ON s.group_id = gr.id
        WHERE gr.group_name = 'Група 2'
        AND sj.subject = 'Географія'
        AND g.grade_date = (
            SELECT MAX(grade_date)
            FROM grades
            WHERE student_id = s.id
            AND subject_id = sj.id
);