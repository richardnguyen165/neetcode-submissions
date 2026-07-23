-- Write your query below

SELECT home_team_id AS team_id, home_team_name AS team_name, (host_points + away_points) AS num_points
FROM (
    SELECT 
    i.home_team_id, 
    i.home_team_name, 
    SUM(i.host_points) AS host_points
    FROM (
        SELECT 
        team_id AS home_team_id, 
        team_name AS home_team_name,
        CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS host_points
        FROM teams t
        LEFT JOIN matches h ON h.host_team = t.team_id
    ) AS i
    GROUP BY i.home_team_name, i.home_team_id
) AS team_1
INNER JOIN (
    SELECT 
    i.away_team_id, 
    i.away_team_name, 
    SUM(i.away_points) AS away_points
    FROM (
        SELECT
        team_id AS away_team_id, 
        team_name AS away_team_name, 
        CASE
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS away_points
        FROM teams t1
        LEFT JOIN matches h1 ON h1.guest_team = t1.team_id
    ) AS i
    GROUP BY i.away_team_name, i.away_team_id
) AS team_2 ON team_2.away_team_id = team_1.home_team_id
ORDER BY num_points DESC, team_id ASC;
