---
title: design semantic in pbi
created: 2025-01-06
updated: 2025-01-06
draft: "true"
---

# Define data granularity

Data granularity is the detail that is represented within your data.
    The more granularity your data has,  the greater the level of detail within your data.
    e.g. the time interval to take aggregate

## Change data granularity to build a relationship between two tables
e.g. 1 table on month granular and 1 table on day. need to link them together to same date dim on either day/ month level. 

## Create a relationship between tables


# Work with relationships and cardinality
## relationship
dim filters fact
ideally not the other way around

1:1 not recommended (redundant information and not designed correctly, best practice to combine the tables)

M:M doesnt require unique values, not recommended due to ambiguity.

## Cross-filter direction
bi directional filter leads to: 
    performance degradation, 
    ambiguity, 
    oversampling, 
    unexpected results

|                  | 1:1 | 1:m | m:m                                 |
| ---------------- | --- | --- | ----------------------------------- |
| single direction | ❌   | ✔   | ✔                                   |
| bi direction     | ✔   | ✔   | ✔(messes with measures and filters) |

# Resolve modeling challenges

circular relationships,


## where to set display folder for columns
model view --> column --> property --> display folder


# Summary
1. What does data granularity mean? 


The level of detail in your data, meaning that higher granularity means more detailed data.

2. What is the difference between a fact table and a dimension table? 

Fact tables contain observational data while dimension tables contain information about specific entities within the data.

3. Choose the best answer to explain relationship cardinality? 

Cardinality is the measure of unique values in a table.
