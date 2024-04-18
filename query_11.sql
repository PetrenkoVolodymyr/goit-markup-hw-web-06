SELECT t.teacher, s.student, ROUND(AVG(m.mark), 2) as avgMark
FROM marks m
INNER JOIN students s ON s.id = m.student_id 
INNER JOIN subjects s2 ON s2.id = m.subject_id 
INNER JOIN teachers t ON t.id = s2.teacher_id  
WHERE m.student_id = 2 AND s2.teacher_id  = 2