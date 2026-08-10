-- Write your query below
SELECT DISTINCT c.title
FROM tv_program tvp
JOIN content c ON c.content_id = tvp.content_id
WHERE c.content_type = 'Movies' AND c.kids_content = 'Y' AND tvp.program_date BETWEEN '2020-06-01 00:00' AND '2020-06-30 23:59';