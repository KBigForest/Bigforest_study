use sakila;
select * from `language` ;


select name from `language` l ;
select language_id, 
	'COMMOM' language_usage,
	language_id * 3.14 lang_pi_value,
	upper(name) language_name
from `language` l ;
select language_id,
	'COMMOM' as language_usage,
	language_id * 3.14 as lang_pi_value,
	upper(name) as language_name
from `language` l ;

select actor_id from film_actor fa order by actor_id;
select distinct actor_id from film_actor fa order by actor_id;

select concat(cust.last_name, ', ', cust.first_name) full_name
from
	(select first_name, last_name, email 
	from customer c 
	where first_name = 'JESSIE'
	) as cust;

select concat(cust.last_name, ', ', cust.first_name) full_name
from
	(select first_name, last_name, email
	from customer c 
	where first_name ='MARY')
	as cust;


create temporary table actor_j
	(actor_id smallint(5),
	first_name varchar(45),
	last_name varchar(45)
);

insert into actor_j
select actor_id, first_name, last_name
from actor where last_name like 'J%';
select * from actor_j;

create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer;

select first_name, last_name  from cust_vw where active = 0;
select * from customer;

select customer.first_name, customer.last_name, 
time(rental.rental_date) as rental_time
from customer inner join rental
on customer.customer_id  = rental.customer_id
where date(rental.rental_date) = '2005-06-14';


select c.first_name,c.last_name,
time(r.rental_date)	as rental_time
from customer as c inner join rental as r
on c.customer_id =	r.customer_id
where date(r.rental_date) =	'2005-06-14';


select title
	from film f 
	where rating = 'G' and rental_duration >=7 ;
	

select title, rating, rental_duration
	from film
	where (rating = 'G' and rental_duration >= 7) 
		or (rating = 'PG-13' and rental_duration <= 3);
		
select c.first_name, c.last_name,  count(*)
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id
group by c.first_name, c.last_name
having count(*) >= 40;

select c.first_name, c.last_name ,
	time(r.rental_date) as rental_time
from customer as c
	inner join rental as r 
	on c.customer_id = r.customer_id
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;




-- 3.1
select a.actor_id, a.first_name, a.last_name  
from actor as a
order by last_name, first_name;
-- 3.2
select a.actor_id, a.first_name, a.last_name
	from actor as a
where a.last_name ='WILLIAMS' or a.last_name  = 'DAVIS'
-- 3.3
select distinct c.customer_id, date(r.rental_date) as rental_date
	from customer as c inner join rental as r
	on c.customer_id = r.customer_id
	where date(r.rental_date) = '2005-07-05'
	order by c.customer_id asc;

-- 3.4
select c.store_id, c.email, date(r.rental_date) 
	as rental_date,
	date(r.return_date) as return_date
from customer as c
	inner join rental as r 
on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by rental_date desc;

select c.email, c.first_name, date(r.rental_date)
from customer as c
	inner join rental as r 
	on c.customer_id = r.customer_id 
	where date(rental_date) <> '2005-06-14';


select title, rating
from film f 
where rating in ('G', 'PG');


select title, rating
from film 
where rating in ('G' 'PG');



select title,	rating
from film
where rating in (select rating	from film where title	like '%PET%');


select title, rating
from film
where title like '%PET%';
from film f 
where rating not in ('PG-13','R', 'NC-17');

select  f.title, f.rating
from film as f 
where f.rating not in ('PG-13','R', "NC-17" );


select left('abcdefg',3)


select last_name, first_name
from customer
where last_name like '_A_T%S';

select last_name, first_name
from customer c 
where last_name like 'Q%' or last_name like 'Y%';

select rental_id, customer_id, return_date
from rental
where return_date is null;

select rental_id,	customer_id,	return_date
from rental
where return_date is not null;


select rental_id, customer_id, return_date
from rental r 
where rental_date is null 
or (date(return_date) not between '2005-05-01' and '2005-08-31')
;

select payment_id,  customer_id, amount, date(payment_date)
from payment p 
where payment_id between 101 and 120;


-- 4.1
select p.payment_id, p.customer_id, amount,date(p.payment_date)
from payment as p
where customer_id != 5 
and amount > 8 and date(payment_date) = '2005-08-23';

-- 4.2
select p.payment_id , p.customer_id, amount,date(p.payment_date)
from payment as p
where (payment_id between 101 and 120)
and customer_id = 5 and not(amount >6 or date(payment_date) = '2005-06-19')

-- 4.3
select amount
from payment p 
where amount in (1.97, 7.98, 9.98);