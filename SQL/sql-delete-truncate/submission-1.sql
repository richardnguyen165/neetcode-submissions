CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO students (id, name)
  VALUES (1, 'Alice'),
         (2, 'Bob'),
         (3, 'Charlie');
-- Do not modify above this line. --

-- TRUCNACATE TABLE more efficient then DELETE FROM because it logs all the table and deletes them all at once, rather than deleting one row at a time
TRUNCATE TABLE students;


-- Do not modify below this line. --
SELECT * FROM students;
