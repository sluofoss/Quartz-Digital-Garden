---
title: Confusing DAX Context Filter
created: 2024-11-28
updated: 2024-11-28
tags:
  - data-analytics
---

# Context: suppose you would like to create a cumulative plot in dax.

i.e. something that is like a ecdf, or total expenditures overtime.

in sql you would do something like a 
```
sum(val) over (
  partition by p
  order by q
  range between unbounded preceeding and current row
)
```
or similar in effect. 

The equivalent in DAX when combined with hidden columns and relationships is somewhat unnatural to think about.

One would have to imagine the following instead.

you first have a x axis of date ( the `q` in order by clause)

then for each measure one would like to plot on the y axis (`sum(val)`),

one would do the following: 

```DAX
calculate(
  sum(table_name[val]),
  table_name[q] <= max(table_name[q])
)
```

Why this works is that in the context filter, RHS is a constant, and since linked to the x axis variable in the visual, it changes from left to right. 

The requirement for this to work properly is to have the filter evaluated as either many to one, or one to one, but never many to many.

The important thing here is that one or all of `table_name[q]` needs to be the same as the column set in the x axis. 

The choice of related `table_name[q]` would affect the range of the plot.
