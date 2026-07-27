-- Write your query below
WITH i AS (
    SELECT sale_date, fruit, sum(sold_num) AS total
    FROM sales
    GROUP BY sale_date, fruit
)
SELECT i.sale_date, i.total - j.total AS diff
FROM i
JOIN i AS j
ON j.sale_date = i.sale_date AND  i.fruit = 'apples' AND j.fruit = 'oranges';