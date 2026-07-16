-- Write your query below
-- Use NOT IN (find all people who do not have their order id in the sales to crimson)

SELECT name 
FROM sales_person
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    LEFT JOIN company c
    ON c.com_id = o.com_id
    WHERE name = 'CRIMSON'
);