1. 

select * from customer_orders;

-- order_date, new_customer_count,repeat_customer_count

-- 2022-01-01 ,3 ,0 
-- 2022-01-02 ,2 ,1
-- 2022-01-03 ,1, 2
------------------------------------------------------
1	100	2022-01-01	2000
2	200	2022-01-01	2500
3	300	2022-01-01	2100
4	100	2022-01-02	2000
5	400	2022-01-02	2200
6	500	2022-01-02	2700
7	100	2022-01-03	3000
8	400	2022-01-03	1000
9	600	2022-01-03	3000
-----------------------------------------------------------------

with first_visit as (
select customer_id, min(order_date) as first_visit_date
from customer_orders
group by customer_id)
, 
visit_flag as (
select co.*, fv.first_visit_date 
, case when co.order_date=fv.first_visit_date then 1 else 0 end as first_visit_flag,
case when co.order_date != fv.first_visit_date then 1 else 0 end as repeat_visit_flag
from customer_orders co
inner join first_visit fv on co.customer_id=fv.customer_id
)

select order_date, sum(first_visit_flag) as no_of_new_customers, sum(repeat_visit_flag) as no_of_repeat_customers
from visit_flag
group by order_date;

-----------------------------------------
2022-01-01	3	0
2022-01-02	2	1
2022-01-03	1	2
---------------------------------


2. 
