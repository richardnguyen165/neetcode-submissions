-- Write your query below
SELECT left_operand, 
operator, 
right_operand, 
CASE
    WHEN operator = '>' THEN left_value > R.value
    WHEN operator = '<' THEN left_value < R.value
    ELSE left_value = R.value
END AS value
FROM (
    SELECT value as left_value, left_operand, operator, right_operand
    FROM variables L
    INNER JOIN expressions E
    ON E.left_operand = L.name) 
AS L2
INNER JOIN variables R
ON L2.right_operand = R.name;