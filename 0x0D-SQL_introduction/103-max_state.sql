-- -- 

SELECT state, MAX(value) AS max_temp
FROM hbtn_0c_0.temperatures
GROUP BY state
ORDER BY state ASC;
