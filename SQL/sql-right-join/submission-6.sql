CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER REFERENCES pokemon_types(id)
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3);
-- Do not modify above this line. --

-- RIGHT JOIN: Same as left join, but all right rows are include, and if there is no match, left values are nulled

SELECT pt.name AS type, p.name AS pokemon, pt.weakness 
FROM pokemon p
RIGHT JOIN pokemon_types pt
ON p.type_id = pt.id
ORDER BY pt.name, p.name, pt.weakness;



