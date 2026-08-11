-- Write your query below
/*
What counts as a consecutive?

1 before it
1 after
1 before it and after it
*/

SELECT c.seat_id
FROM cinema c
LEFT JOIN cinema c1 ON c1.seat_id + 1 = c.seat_id
LEFT JOIN cinema c2 ON c2.seat_id - 1 = c.seat_id
WHERE (c1 IS NOT NULL AND c1.free = 1 AND c.free = 1) OR (c2 IS NOT NULL AND c2.free = 1 AND c.free = 1)
ORDER BY seat_id;