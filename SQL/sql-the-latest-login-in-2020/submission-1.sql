-- Write your query below
SELECT a.user_id, MAX(a.time_stamp) AS last_stamp
FROM (
    SELECT *
    FROM logins
    WHERE time_stamp BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59'
) AS a
GROUP BY (a.user_id);