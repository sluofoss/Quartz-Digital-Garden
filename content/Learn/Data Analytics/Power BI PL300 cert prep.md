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

### formal dev workflow (report building steps in power bi)
1. building the data model and analyzing data
2. report design
3. preparing to share your report
4. sharing report with stakeholders

## Power BI Service

## asset maintenance
### valid methods to grant user real-only permission to access a dataset
| valid | invalid |
|- |- |
| Grant access to an app and let the user get the app | Include the user in the workspace contact list |
| Directly grant access to the user | Assign the user to a row-level security role |
| Share via link a report which uses the dataset| | 


### permission with activity
| read | buiid | reshare | write |
|-|-|-|-|
|The CEO needs to see the data in the company financials report|A data analyst would like to create a new report using this dataset|A Power BI report designer wants to provide read access to the accounting team|A Power BI report designer would like to feature specific Q&A questions on all reports which use this dataset|
||A developer wants to query our dataset by using its external API||A DBA re-wrote several queries to fix performance problems and needs to replace the dataset with a new one|

### ???
endorsing content in power bi
datasets, dataflows, reports, and apps
not dashboards.

### subscription
- subscription allowed for report , paginated report + normal , 
- hidden tabs cant be shared via subscription
- power bi subscription doesnt directly interact with slack api so auto alert/refresh notification is not directly possible.

### promote vs certify
promote
- Everybody in an organization with write permissions on a workspace may perform this action.
- A data consumer wants to bring awareness to an interesting dataset.
- The key consideration is, "This content is good enough to share.

certify

- The Power BI Center of Excellence wishes to use this dataset as a model for the organization.
- Only a select group of reviewers may perform this action.
- The key consideration is, "This content is reliable, authoritative content ready to use across the organization.

### steps to enable certify content in admin
Navigate to the Power BI admin portal.

In the Certification menu, enable certification and add the Power BI Certifiers group. Apply the changes.

Navigate to the workspace containing content for certification.

Open the Settings for the content you wish to certify.

In the endorsements section, choose "Certified" and apply the changes.

### customization
- report setting can allow viewer to personalize visual when accessed in pbi service


