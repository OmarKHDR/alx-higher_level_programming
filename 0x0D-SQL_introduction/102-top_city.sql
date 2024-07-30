-- --

SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3
