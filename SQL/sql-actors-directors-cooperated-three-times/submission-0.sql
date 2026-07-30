-- Write your query below
SELECT ad.actor_id, ad.director_id
FROM actor_director ad
GROUP BY ad.actor_id, ad.director_id
HAVING COUNT(*) >= 3;