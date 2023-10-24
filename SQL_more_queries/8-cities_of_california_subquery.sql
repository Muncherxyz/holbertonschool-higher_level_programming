-- Select cities from cities where statie_id = (select id from states where name = 'california')
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'california');
