CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

INSERT INTO students (id, name, age) VALUES
(1, 'Alice', 20),
(2, 'Bob', NULL),
(3, 'Charlie', 30);
-- Do not modify above this line. --

-- We can update all rows using UPDATE and SET statements.
-- Use the columnn name to set all the columns value to a specific value, plus also by using the equal sign
UPDATE students
SET age = NULL;

-- Do not modify below this line. --
SELECT * FROM students;
