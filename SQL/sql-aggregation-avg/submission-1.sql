CREATE TABLE scores (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    score INTEGER,
    subject TEXT
);

INSERT INTO scores (score, subject) VALUES
(72, 'math'),
(88, 'math'),
(68, 'math'),
(80, 'science'),
(90, 'science'),
(60, 'science'),
(90, 'history'),
(85, 'history'),
(100, 'history');
-- Do not modify above this line. --

-- AVG - helps find the average values in a column, will ignore null values
-- default - returns a floating-point number, use ROUND to round floating point numbers

SELECT ROUND(AVG(score)) AS average_math_score
FROM scores
WHERE subject = 'math';



