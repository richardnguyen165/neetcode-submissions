-- Write your query below
-- Review
SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM employees
GROUP BY (day, emp_id);