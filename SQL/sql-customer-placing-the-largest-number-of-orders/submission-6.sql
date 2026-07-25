-- Write your query below
SELECT o.customer_number
FROM orders o
GROUP BY o.customer_number
ORDER BY COUNT(o.order_number) DESC
LIMIT 1; -- Just get the first row