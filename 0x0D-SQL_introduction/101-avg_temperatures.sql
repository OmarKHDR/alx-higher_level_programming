-- name

SELECT city ,AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
