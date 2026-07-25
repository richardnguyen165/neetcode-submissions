-- Write your query below
SELECT o1.customer_number
FROM (
    SELECT o2.customer_number, COUNT(o2.order_number) AS order_number
    FROM orders o2
    GROUP BY o2.customer_number
) AS o1
WHERE o1.order_number >= ALL(
  SELECT COUNT(o3.order_number) AS order_number
  FROM orders o3
  GROUP BY o3.customer_number
);