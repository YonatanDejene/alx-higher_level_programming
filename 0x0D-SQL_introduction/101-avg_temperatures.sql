-- Displays the average temperature (in Fahrenheit) by city.
-- Ordered by descending temperature.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;