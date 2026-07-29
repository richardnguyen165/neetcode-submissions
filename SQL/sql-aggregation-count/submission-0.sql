CREATE TABLE books (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title TEXT,
    author TEXT
);

INSERT INTO books (title, author) VALUES
    ('The Great Gatsby', 'F. Scott Fitzgerald'),
    ('To Kill a Mockingbird', 'Harper Lee'),
    ('Woolbur', 'Harper Lee'),
    ('1984', 'George Orwell'),
    ('Pride and Prejudice', 'Jane Austen'),
    ('The Catcher in the Rye', 'J.D. Salinger'),
    ('The Lord of the Rings', 'J.R.R. Tolkien'),
    ('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling'),
    ('Harry Potter and the Chamber of Secrets', 'J.K. Rowling'),
    ('The Shining', 'Stephen King'),
    ('The Da Vinci Code', 'Dan Brown'),
    ('The Alchemist', 'Paulo Coelho'),
    ('The Picture of Dorian Gray', 'Oscar Wilde');
-- Do not modify above this line. --



/*
What if we wan to count the number of likes for the tweet with id 1, use COUNT function

SELECT COUNT(*)
FROM likes
WHERE tweet_id = 1;

Trhis is for counting the number of distinct tweets the user liked
SELECT COUNT(DISTINCT liked_by_id)
FROM likes
WHERE tweet_id = 1;
*/

SELECT COUNT(DISTINCT author) AS unique_authors
FROM books
WHERE LENGTH(author) < 12;

