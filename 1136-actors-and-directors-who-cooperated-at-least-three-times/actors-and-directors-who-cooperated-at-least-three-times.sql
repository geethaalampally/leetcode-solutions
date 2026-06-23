-- SELECT actor_id, director_id
-- FROM (
--     SELECT actor_id,
--            director_id,
--            COUNT(*) AS score
--     FROM ActorDirector
--     GROUP BY actor_id, director_id
--     HAVING COUNT(*) >= 3
-- ) temp;

SELECT actor_id,
       director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;