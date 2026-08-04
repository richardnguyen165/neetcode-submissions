-- Write your query below
-- Review
SELECT e.left_operand, e.operator, e.right_operand,
CASE 
    WHEN e.operator = '=' THEN l.value = r.value
    WHEN e.operator = '>' THEN l.value > r.value
    ELSE l.value < r.value
END AS value
FROM expressions e
JOIN variables l ON l.name = e.left_operand
JOIN variables r ON r.name = e.right_operand;
