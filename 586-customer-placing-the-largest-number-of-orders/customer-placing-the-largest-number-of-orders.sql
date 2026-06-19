-- select customer_number from 
-- (
-- select customer_number , count(*) as total_orders 
-- from orders
-- group by customer_number 
-- ) t
-- order by t.total_orders desc 
-- limit 1;

SELECT customer_number
FROM Orders 
GROUP BY customer_number
ORDER BY count(customer_number) DESC
LIMIT 1