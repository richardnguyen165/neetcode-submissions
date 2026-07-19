/*
INSERT DEFAULT VALUES

You can omit values for columns that have default values
*/

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --

INSERT INTO products (id, name)
    values (1, 'Apple'), (2, 'Banana'), (3, 'Orange');






-- Do not modify below this line --
SELECT * FROM products;
