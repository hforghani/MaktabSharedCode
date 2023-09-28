\c testdb

create table users ( 
id serial primary key, 
username varchar(100) not null 
);
-- serial: integer NOT NULL DEFAULT nextval('table_name_id_seq')
-- primary key: unique, not null


insert into users (id, username) values
(1, 'ali'),
(2, 'hossein'),
(3, 'jamshid');

insert into users (username) values
('sara'),
('fateme'),
('morad');


insert into users (username) values ('hamid');

ALTER TABLE users ALTER COLUMN id TYPE integer NOT NULL DEFAULT nextval('users_id_seq');


delete from users where username in ('fateme', 'morad');


ALTER TABLE users
ADD CONSTRAINT users_pk PRIMARY KEY (id);


create table ProjectEmplooye (
	id int primary key,
	project_id int not null,
	employee_id int not null,
	CONSTRAINT fk_project
	      FOREIGN KEY(project_id) 
	      REFERENCES projects(id),
	CONSTRAINT fk_employee
	      FOREIGN KEY(employee_id) 
	      REFERENCES employees(id),
	-- CONSTRAINT primary key (project_id, employee_id) -- unique, not null
);


-- group by, order

select category_id from category where name='Drama';

select film_id from film_category where category_id=7


select * from film where film_id in (
	select film_id from film_category where category_id=(
		select category_id from category where name='Drama'
	)
);

--select * from film
--join film_category on film.film_id = film_category.film_id
--join category on category.category_id = film_category.category_id
--where category.name = 'Drama';


-- هر category_id چند تا film داره؟

-- category_id	count
-- 1		11
-- 2		14
-- 3		100


-- aggregate function: count, sum, avg, min, max

select category_id, count(film_id) as film_count
from film_category
group by category_id
order by film_count desc;

-- ۵ تا category_id که بیشترین تعداد فیلم را دارند؟

select category_id from (
	select category_id, count(film_id) as film_count
	from film_category
	group by category_id
	order by film_count desc
	limit 5
);


-- payment: customer_id, amount
-- مجموع خریدهای هر customer_id
select customer_id, min(amount)
from payment
group by customer_id;



select city.city
from city join country
on city.country_id = country.country_id
where country.country = 'Iran';

-- نام و نام خانوادگی مشتریهای کشور آمریکا رو بده.

select customer.first_name, customer.last_name
from 
customer join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
join country on city.country_id = country.country_id
where country.country = 'United States';

---- 2
select cu.first_name, cu.last_name
from 
customer cu join address ad on cu.address_id = ad.address_id
join city ci on ad.city_id = ci.city_id
join country co on ci.country_id = co.country_id
where co.country = 'United States';


-- inner/left/right/full outer    join
A cross join B
where A.name = B.name

A full outer join B
on A.name = B.name

-- Cartesian Product
select ???
from A , B
where A.name = B.name;

-- چند مشتری از هر کشور به ترتیب از زیاد به کم؟

select co.country, count(cu.customer_id) as cust_count
from 
customer cu join address ad on cu.address_id = ad.address_id
join city ci on ad.city_id = ci.city_id
join country co on ci.country_id = co.country_id
group by co.country_id  -- co.country
order by cust_count desc;	


-- co.country_id : int , primary key (+index)
-- co.country:     varchar

-- مشتریهای هندی فیلمهای به چه زبانی را اجاره کرده اند؟

select distinct la.name

from
customer cu join address ad on cu.address_id = ad.address_id
join city ci on ad.city_id = ci.city_id
join country co on ci.country_id = co.country_id
join rental re on cu.customer_id = re.customer_id
join inventory iv on iv.inventory_id = re.inventory_id
join film fi on fi.film_id = iv.film_id
join language la on la.language_id = fi.language_id

where co.country = 'Italy';

-- مشتریهای هندی فیلمهای چه ژانری را اجاره کرده اند؟


select distinct ca.name

from
customer cu join address ad on cu.address_id = ad.address_id
join city ci on ad.city_id = ci.city_id
join country co on ci.country_id = co.country_id
join rental re on cu.customer_id = re.customer_id
join inventory iv on iv.inventory_id = re.inventory_id
join film fi on fi.film_id = iv.film_id
join film_category fc on fc.film_id = fi.film_id
join category ca on ca.category_id = fc.category_id

where co.country = 'India';

-- مشتریهای هندی از هر ژانری چندتا اجاره کرده اند؟


select ca.name, count(re.rental_id)

from
customer cu join address ad on cu.address_id = ad.address_id
join city ci on ad.city_id = ci.city_id
join country co on ci.country_id = co.country_id
join rental re on cu.customer_id = re.customer_id
join inventory iv on iv.inventory_id = re.inventory_id
join film fi on fi.film_id = iv.film_id
join film_category fc on fc.film_id = fi.film_id
join category ca on ca.category_id = fc.category_id

where co.country = 'India'
group by ca.category_id;



-- ساختن index دوتایی

CREATE INDEX film_title_rating
ON film (title, rating);


select sum(amount) from payment;


-- مجموع پرداختی هر فیلم را بده.

select fi.title, sum(pa.amount)
from
film fi join inventory iv on fi.film_id = iv.film_id
join rental re on re.inventory_id = iv.inventory_id
join payment pa on pa.rental_id = re.rental_id
group by fi.film_id
order by sum desc;

