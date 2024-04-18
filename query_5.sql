SELECT t.teacher, s.topics 
FROM teachers  AS t
INNER JOIN subjects AS s ON t.id = s.teacher_id 
ORDER by t.teacher 