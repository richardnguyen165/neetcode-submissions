-- Write your query below
SELECT DISTINCT seller_name
FROM seller s
LEFT JOIN (
    SELECT *
    FROM orders o
    WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
) AS i
ON s.seller_id = i.seller_id
WHERE order_id IS NULL;