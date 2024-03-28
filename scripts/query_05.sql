SELECT s.subject
        FROM subjects s
        JOIN teachers t ON s.teacher_id = t.id
        WHERE t.fullname = 'Іванов Іван';