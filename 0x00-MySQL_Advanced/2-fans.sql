-- A  SQL script that ranks country origins of bands, ordered
-- by the number of (non-unique) fans

SELECT origin,SUM(nb_fans) AS total_fans
FROM metal bands
GROUP BY origin;
