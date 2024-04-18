SELECT s.student , ROUND(AVG(mark), 2) as avgMark
FROM marks m
INNER JOIN students s ON s.id = m.student_id 
GROUP by student_id 
ORDER by avgMark DESC
LIMIT 5