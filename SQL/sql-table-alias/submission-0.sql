CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE employment_records (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    company_name TEXT,
    job_title TEXT
);


INSERT INTO users (id, name, email) VALUES
(1, 'Alice', 'alice@gmail.com'),
(2, 'Bob', 'bob@gmail.com'),
(3, 'Charlie', 'charlie@gmail.com');

INSERT INTO employment_records (id, user_id, company_name, job_title) VALUES
(100, 1, 'Google', 'Software Engineer'),
(300, 2, 'Microsoft', 'Data Scientist'),
(500, 3, 'Amazon', 'Product Manager');
-- Do not modify above this line. --

-- AS (table alias)

SELECT u.name, u.email, er.company_name, er.job_title
FROM users u
INNER JOIN employment_records er
ON er.user_id = u.id
ORDER BY er.company_name;




