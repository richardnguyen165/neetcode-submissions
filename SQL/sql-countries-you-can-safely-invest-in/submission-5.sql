-- Write your query below
SELECT i.country
FROM (SELECT co.name as country, AVG(c.duration) AS avg_duration
FROM person p
JOIN calls c ON c.caller_id = p.id OR c.callee_id = p.id
JOIN country co ON co.country_code = SUBSTRING(p.phone_number, 1, 3)
GROUP BY co.name) AS i
WHERE i.avg_duration > ALL(
    SELECT (SUM(duration) * 2) / (COUNT(*) * 2) as avg_duration
    FROM calls
);