CREATE TYPE status AS ENUM ('active', 'inactive', 'pending');
-- Constraints must be followed

CREATE TABLE users (
    id INTEGER PRIMARY KEY, -- id must be unique and non-empty 
    name TEXT NOT NULL, -- name must be non-empty
    age INTEGER CHECK (age >= 18), -- age must be at least 18
    status status -- status can only have values active, inactive, and pending
);
-- Do not modify above this line --


INSERT INTO users (id, name, age, status) VALUES
  (1, 'John Doe', 20, 'active'),
  (2, 'Jane Doe', 27, 'pending'),
  (3, 'John Smith', 28, 'active'),
  (4, 'Jane Smith', 30, 'inactive');


-- Do not modify below this line --
SELECT * FROM users;
