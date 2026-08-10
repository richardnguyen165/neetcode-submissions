-- Write your query below

SELECT DISTINCT ON (student_id)
student_id, exam_id, score
FROM exam_results er
ORDER BY er.student_id ASC, er.score DESC, er.exam_id ASC;