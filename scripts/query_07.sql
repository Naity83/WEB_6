SELECT s.fullname, g.grade
        FROM grades g
        JOIN students s ON g.student_id = s.id
        JOIN subjects subj ON g.subject_id = subj.id
        JOIN groups grp ON s.group_id = grp.id
        WHERE grp.group_name = 'Група 2' AND subj.subject = 'Фізика';