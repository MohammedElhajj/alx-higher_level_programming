-- All records of the table second_table listed by descending score
-- Display the score and the name. Don’t list rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
