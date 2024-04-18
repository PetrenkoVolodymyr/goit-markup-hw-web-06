SELECT t.teacher, s.topics, ROUND(AVG(m.mark), 2) as avgMark 
FROM marks m
INNER JOIN subjects s ON s.id = m.subject_id 
INNER JOIN teachers t ON t.id = s.teacher_id  
WHERE s.teacher_id  = 2
GROUP by m.subject_id 
ORDER by s.topics 