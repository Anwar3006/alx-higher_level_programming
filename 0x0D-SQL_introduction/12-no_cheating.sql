-- Script that updates the score of Bob to 10 in the table second_table
UPDATE `second_table`
SET `name` = 10
WHERE `name` = 
(
    SELECT `score`
    FROM `second_table`
    WHERE `name` = 'Bob'
);
