SELECT s2.topics, student, m.mark
FROM marks AS m
INNER JOIN students s ON s.id = m.student_id 
INNER JOIN subjects s2 ON s2.id = m.subject_id 
WHERE s2.id = 2