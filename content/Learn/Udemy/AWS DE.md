---
title: AWS DE
created: 2024-09-30T21:35
updated: 2024-10-10T00:04
draft: "true"
---


select *
from titanic
limit 10;

select avg(Survived)
from titanic;

select avg(case when (Sex = 'female') or (Age <= 12) then Survived end ) as women_children_rate
from titanic;

select avg(case when (Sex != 'female') and (Age > 12) then Survived end ) as others_rate
from titanic;
