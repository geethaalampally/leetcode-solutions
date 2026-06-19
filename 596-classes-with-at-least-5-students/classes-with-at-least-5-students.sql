# Write your MySQL query statement below
select class from (
    select *
    from Courses
    group by class
    having count(*) >= 5

) t;
