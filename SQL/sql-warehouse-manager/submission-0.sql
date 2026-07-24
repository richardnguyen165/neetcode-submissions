-- Write your query below
SELECT w.name as warehouse_name, SUM(width * length * height * units) as volume
FROM warehouse w
JOIN products p ON w.product_id = p.product_id
GROUP BY w.name;