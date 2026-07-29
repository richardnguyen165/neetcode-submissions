-- Write your query below
SELECT u.name, SUM(t.amount) as BALANCE
FROM users u
JOIN transactions t
ON u.account = t.account
GROUP BY u.name
HAVING SUM(t.amount) > 10_000;