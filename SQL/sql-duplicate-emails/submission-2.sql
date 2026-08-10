-- Write your query below
SELECT p.email
FROM person p
GROUP BY p.email
HAVING COUNT(p.email) > 1;