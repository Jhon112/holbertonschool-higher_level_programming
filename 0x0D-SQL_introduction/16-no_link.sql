-- list all records of table.
-- don't show rows without name
SELECT score, name FROM second_table
WHERE name is not NULL
ORDER BY score DESC
