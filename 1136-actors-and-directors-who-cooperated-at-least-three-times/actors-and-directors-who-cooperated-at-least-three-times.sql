-- SELECT actor_id, director_id
-- FROM (
--     SELECT actor_id,
--            director_id,
--            COUNT(*) AS score
--     FROM ActorDirector
--     GROUP BY actor_id, director_id
--     HAVING COUNT(*) >= 3
-- ) temp;

select actor_id , director_id
from ActorDirector
group by actor_id , director_id
having count(*)>2;