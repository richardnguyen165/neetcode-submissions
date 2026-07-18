-- Write your query below
SELECT u.name, COALESCE(l.sum, 0) AS travelled_distance
FROM users u
LEFT JOIN (
    SELECT r.user_id, SUM(r.distance)
    FROM rides r
    GROUP BY r.user_id
) AS l
ON u.id = l.user_id
ORDER BY travelled_distance DESC, u.name;