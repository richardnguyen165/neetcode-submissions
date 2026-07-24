CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    total_price DECIMAL(10, 2) NOT NULL
);

INSERT INTO users (user_id, name) VALUES
(1, 'John'),
(2, 'Jane');

INSERT INTO orders (order_id, user_id, total_price) VALUES
(1, 1, 100.00),
(2, 2, 200.00);
-- Do not modify above this line. --

-- Joins allows us to combine two tables

-- CROSS JOIN: cartesian product

SELECT u.user_id, u.name, o.order_id, o.total_price
FROM users u
CROSS JOIN orders o
WHERE u.user_id = o.order_id;




