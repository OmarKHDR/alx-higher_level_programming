-- --

SELECT cities.id, cities.name
FROM cities
RIGHT JOIN states
ON cities.state_id = states.id
