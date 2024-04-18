SELECT s2.topics , g.groups , ROUND(AVG(m.mark), 2) as avgMark
FROM marks m
INNER JOIN subjects s2 ON s2.id = m.subject_id 
INNER JOIN students AS s ON s.id = m.student_id 
INNER JOIN groups g ON g.id = s.gruop_id  
WHERE subject_id  = 3
GROUP by s.gruop_id 