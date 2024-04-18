SELECT g.groups, s2.topics, s.student, m.mark, m.marker_at 
FROM marks m
INNER JOIN students s ON s.id = m.student_id 
INNER JOIN subjects s2 ON s2.id = m.subject_id 
INNER JOIN teachers t ON t.id = s2.teacher_id  
INNER JOIN groups g ON g.id = s.gruop_id 
WHERE g.id = 1 AND s2.id = 2 AND m.marker_at = (SELECT MAX(m.marker_at) FROM marks m)
ORDER by m.marker_at DESC