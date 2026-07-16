/*
Booleans are a type of data that can only be true or false

true = TRUE, true, t, y, 1
false = FALSE, false, f, n, 0

Best practice: Use TRUE/FALSE, true/false
*/

CREATE TABLE three_column_table (
  id INTEGER PRIMARY KEY,
  is_active BOOLEAN,
  is_admin BOOLEAN
);






-- Do not modify below this line --
INSERT INTO three_column_table (id, is_active, is_admin) 
  VALUES (1, TRUE, FALSE),
         (2, true, false),
         (3, 't', 'f'),
         (4, 'y', 'n'),
         (5, 'yes', 'no'),
         (6, 'on', 'off'),
         (7, '1', '0');

SELECT * FROM three_column_table;
