SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id from orders)
