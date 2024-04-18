SELECT g.groups , student 
FROM students s 
INNER JOIN groups g ON g.id = s.gruop_id  
WHERE gruop_id =1