-- Write your query below
SELECT
CASE 
    WHEN from_id > to_id THEN to_id
    ELSE from_id
END AS person1,
CASE 
    WHEN from_id < to_id THEN to_id
    ELSE from_id
END AS person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM calls
GROUP BY (person1, person2);
