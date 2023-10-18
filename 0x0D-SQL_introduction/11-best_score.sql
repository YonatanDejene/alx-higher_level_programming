-- Lists all records in the table named second_table with a score >= 10 in MySQL server.
-- Ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;