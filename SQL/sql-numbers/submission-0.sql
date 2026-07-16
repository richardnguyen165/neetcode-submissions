/*
How to represent numbers in PostgreSQL

Integers:
SMALLINT: -32768 TO 32767 (2 BYTE = 16 BITS)
INTEGER: -2147483648 TO 2147483647 (4 BYTE = 32 BITS)
BIGINT: -9223372036854775808 TO 9223372036854775807 (8 BYTE = 64 BITS)

Floating-point numbers:
FLOAT (4 BYTE FLOATING POINT NUMBER)
DOUBLE PRECISION (8 BYTE FLOATING POINT NUMBER)
DECIMAL (FIXED-POINT NUMBER, PRECISION SPECIFIED UP TO THE NUMBER OF DIGITS RIGHT OF DECIMAL POINT AND NUMBER OF DIGITS STORED)
NUMERIC IS IDENTICAL TO DECIMAL

CREATE TABLE numbers_table (
  small_int_column SMALLINT,
  int_column INTEGER
  big_int_column BIGINT
  float_column FLOAT
  double_column DOUBLE PRECISION,
  decimal_column DECIMAL(10, 2),
  numeric_column NUMERIC(10, 1)
)
*/



CREATE TABLE bank_accounts (
  id BIGINT PRIMARY KEY,
  balance NUMERIC(20, 2),
  interest_rate NUMERIC(5, 2),
  number_of_owners SMALLINT
);







-- Do not modify below this line --
INSERT INTO bank_accounts (id, balance, interest_rate, number_of_owners) VALUES
    (1, 123451234512345123.45, 123.45, 1);

SELECT 
    ba.*,
    (SELECT STRING_AGG(column_name || ' ' || data_type || CASE WHEN numeric_precision IS NOT NULL THEN '(' || numeric_precision || ',' || numeric_scale || ')' ELSE '' END, ', ')
     FROM information_schema.columns 
     WHERE table_name = 'bank_accounts') AS column_types
FROM 
    bank_accounts ba;
