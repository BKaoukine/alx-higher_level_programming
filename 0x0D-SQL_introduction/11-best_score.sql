-- script that lists all records with a score >= 10 in table second_table of the database
        -- Results should display both the score and the name (in this order)
        -- Records should be ordered by score (top first)

SELECT score, name FROM second_table HAVING score >= 10 ORDER BY score DESC;
