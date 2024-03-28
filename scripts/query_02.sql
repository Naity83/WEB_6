SELECT s.id, s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sj ON g.subject_id = sj.id
WHERE sj.subject = 'Математика'
GROUP BY s.id, s.fullname
ORDER BY avg_grade DESC
LIMIT 1;