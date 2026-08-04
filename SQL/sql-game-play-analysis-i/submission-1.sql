-- Write your query below
SELECT a.player_id, MIN(a.event_date) AS first_login
FROM activity a
GROUP BY a.player_id;