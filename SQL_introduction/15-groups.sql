-- Selects the number of records with same score in table
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
