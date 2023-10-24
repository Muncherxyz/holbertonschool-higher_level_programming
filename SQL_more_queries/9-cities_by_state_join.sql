-- Select cities from cities where statie_id = (select id from states where name = 'california')
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON state_id = states.id;
