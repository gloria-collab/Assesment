
---ASSESSMENT Display in descending order of seniority the male employees whose net salary (salary + commission) is greater than or equal to 8000.
--The resulting table should include the following columns: Employee Number, First Name and Last Name, Age, and Seniority.
SELECT first_name, last_name 
FROM EMPLOYEES
WHERe (salary + commission) >= 8000;

select *, (salary + commission) as net_com
from employees


--question 2
/* Display products that meet the following criteria: (C1) quantity is packaged in bottle(s), (C2) the third character in the product name is 't' or 'T', 
(C3) supplied by suppliers 1, 2, or 3, (C4) unit price ranges between 70 and 200, and (C5) units ordered are specified (not null). 
The resulting table should include the following columns: product number, product name, supplier number, units ordered, and unit price. */

select product_name, supplier_int, units_on_order, unit_price, product_ref
from products
where quantity ilike '%bottles%' 
and product_name ilike '__t' 
and supplier_int in (1, 2, 3) and unit_price between 70 and 200
and units_on_order is not null
group by product_ref, product_name, supplier_int, units_on_order, unit_price;

/* question 3
Display customers who reside in the same region as supplier 1, meaning they share the same country, city, and the last three digits of the postal code. 
The query should utilize a single subquery. The resulting table should include all columns from the customer table.*/

select distinct(concat(country,' ',city)), phone,fax, customer_code,company, address, postal_code
from customers
where country=(
	select country
	from suppliers
	where supplier_int= 1 )
and city=(select city
			from suppliers
			where supplier_int= 1)
and right(postal_code, 3) =(
						select right(postal_code,3) 
						from suppliers
						where supplier_int = 1);

/* Queston 3
For each order number between 10998 and 11003, do the following:  
-Display the new discount rate, which should be 0% if the total order amount before discount (unit price * quantity) 
is between 0 and 2000, 5% if between 2001 and 10000, 10% if between 10001 and 40000, 15% if between 40001 and 80000, and 20% otherwise.
-Display the message "apply old discount rate" if the order number is between 10000 and 10999, and "apply new discount rate" otherwise. 
The resulting table should display the columns: order number, new discount rate, and discount rate application note.
*/

select order_int,discount as new_discount_rate,
case
when order_int between 10000 and 10999 then 'new discount rate'
else 'old discount rate'
end
from order_details;

/*
-Display the new discount rate, which should be 0% if the total order amount before discount (unit price * quantity) is between 0 and 2000, 5% if between 2001 and 10000, 
10% if between 10001 and 40000, 
15% if between 40001 and 80000, and 20% otherwise.
*/
select discount, (unit_price * quantity) as total_order,
	case
	when (unit_price * quantity) between 0 and 2000 then 0
	when (unit_price * quantity) between 2001 and 10000 then 5
	when (unit_price * quantity) between 10001 and 40000 then 10
	when (unit_price * quantity) between 40001 and 80000 then 15
	else 20
	end
from order_details;



--question 4
--Display suppliers of beverage products. The resulting table should display the columns: supplier number, company, address, and phone number.
select category_code,company, address, phone number,s.supplier_int
from products as p
full outer join  suppliers as s
on p.supplier_int = s.supplier_int
where category_code = 1
order by p.supplier_int;

--question 5
--Display customers from Berlin who have ordered at most 1 (0 or 1) dessert product. The resulting table should display the column: customer code.
UPDATE customers
set country ='Berlin'
where country ='Brésil';

select *
from products
where category_code = 3 
and products.units_on_order IS NOT NULL;


select *
from customers as c
join 
	orders as o
on c.customer_code = o.customer_code
join 
	order_details as od
on o.order_int= od.order_int
where country = 'Berlin';



----question 6
-- Display customers who reside in France and the total amount of orders they placed every Monday in April 1998 (considering customers who haven't placed any orders yet). 
-- The resulting table should display the columns: customer number, company name, phone number, total amount, and country.
select c.customer_code, c.company, c.country,count(o.customer_code) cust_c
from customers as c
left join orders as o
on o.customer_code = c.customer_code
AND order_date >='1998-04-01'
where country ='France'
group by c.customer_code, c.country;


--question 7 Display customers who have ordered all products. The resulting table should display the columns: customer code, company name, and telephone number
SELECT c.customer_code, c.company, c.phone
FROM customers AS c
WHERE NOT EXISTS (
    SELECT p.product_ref
    FROM products AS p
    WHERE NOT EXISTS (
        SELECT 1, *
        FROM orders AS o
        JOIN order_details AS od ON o.order_int = od.order_int
        WHERE o.customer_code = c.customer_code
        AND od.product_ref = p.product_ref
    )
);

-- Display for each customer from France the number of orders they have placed. The resulting table should display the columns: customer code and number of orders.
select c.customer_code, count(order_int) as num_of_orders
from customers as c
left join orders as o
on c.customer_code = o.customer_code
where c.country = 'France'
group by c.customer_code;



--Display the number of orders placed in 1996, the number of orders placed in 1997,
--and the difference between these two numbers. The resulting table should display the columns: orders in 1996, orders in 1997, and Difference.
SELECT 
    COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 1996 THEN 1 END) AS orders_in_1996,
    COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 1997 THEN 1 END) AS orders_in_1997,
    COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 1997 THEN 1 END) -
    COUNT(CASE WHEN EXTRACT(YEAR FROM order_date) = 1996 THEN 1 END) AS difference
FROM orders;
