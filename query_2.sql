SELECT s2.topics , s.student , ROUND(AVG(mark), 2) as avgMark
FROM marks m
INNER JOIN students s ON s.id = m.student_id 
INNER JOIN subjects s2 ON s2.id = m.subject_id 
WHERE subject_id = 1
GROUP by student_id 
ORDER by avgMark DESC
LIMIT 1