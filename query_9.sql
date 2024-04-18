SELECT s.student , s2.topics 
FROM marks m
INNER JOIN students s ON s.id = m.student_id 
INNER JOIN subjects s2 ON s2.id = m.subject_id 
WHERE student_id = 2
GROUP by subject_id 
ORDER by s2.topics 