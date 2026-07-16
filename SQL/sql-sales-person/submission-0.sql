-- Write your query below
SELECT sp.name
FROM sales_person sp
LEFT JOIN (
    SELECT *
    FROM company c
    LEFT JOIN orders o
    ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
) AS s
ON s.sales_id = sp.sales_id
WHERE s.sales_id IS NULL;
