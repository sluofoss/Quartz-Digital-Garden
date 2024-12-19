---
title: Power BI PL300 cert prep
created: 2024-12-19
updated: 2024-12-19
tags:
  - data-analytics
  - powerbi
---

# Prepare Data for Analysis
## Power Query


# Model data 

## power bi vs power bi service

pbi service is software as service, pbi desktop is not.

| pbi desktop | both | pbi service |
| - | - | - |
|many data sources | reports | some data sources |
| transforming | visualization | dashboards
| shaping & modeling | security | apps & workspaces |
| measures | filters | sharing |
| calculated columns | bookmarks | dataflow creation |
| python | qa | paginated reports |
| themes | r visuals | rls management |
| rls creation | | gateway connections | 

## DAX
row context
- the context which a atomic row level calculation takes place in. will ever focus on a single row.


filter context
- the context which filters a list of rows into a subset. This creates a bound for whatever row context needs to happen in.


context transition:
- converts row context to column context such that one can chain different filters and evaluate different groups, sort of like
  - group by some related columns from other table or
  - group by some derived value which now serves as extra context?


4 important concept in dax
- evaluation contexts
- iterators
- context transition
- expanded tables
> https://www.sqlbi.com/tv/7-reasons-dax-is-not-easy/
> dax 101 sqlbi

# Build Visual and reports
## Power BI Desktop

## report design in power bi

## concept of progressive disclosure

## mobile layout for report design
- prioritize key metrics first
  - avoid more than 4 metrics
  - summarize display units to save space
  - abbreviate measure names
- implement focal point tracking
  - use the z layout
    - focus on top
    - scan through the middle
    - read carefully at the end
- consider orientation
- consider visual

- visuals will be shown or hidden on the mobile layout based on whether they are currently visible or hidden on the desktop layout.
  - hence desktop and mobile should be designed differently using separate pages?


# Manage workplace and datasets
## Power BI Service

