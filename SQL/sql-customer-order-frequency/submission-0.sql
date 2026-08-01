-- Write your query below
SELECT i2.customer_id, i2.name
FROM(
    SELECT customer_id, name, month_value
    FROM (SELECT 
        c.customer_id, 
        c.name, 
        o.product_id, 
        o.quantity,
        CASE
            WHEN o.order_date < '2020-08-01' AND        o.order_date > '2020-06-30' THEN 6
            ELSE 7
        END AS month_value
    FROM customers c
    JOIN orders o
    ON o.customer_id = c.customer_id
    WHERE o.order_date < '2020-08-01' AND o.order_date > '2020-05-31') AS i
    JOIN product p
    ON p.product_id = i.product_id
    GROUP BY customer_id, name, month_value
    HAVING SUM(i.quantity * p.price) >= 100
) i2
GROUP BY i2.customer_id, i2.name
HAVING COUNT(i2.name) = 2;
