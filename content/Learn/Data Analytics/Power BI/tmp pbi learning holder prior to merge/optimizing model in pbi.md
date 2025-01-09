---
title: optimizing model in pbi
created: 2025-01-08
updated: 2025-01-08
draft: true
---
methods:
- Ensuring that the correct data types are used.
- Deleting unnecessary columns and rows.
- Avoiding repeated values.
- Replacing numeric columns with measures.
- Reducing cardinalities.
- Analyzing model metadata.
- Summarizing data where possible.

goal:
- Review the performance of measures, relationships, and visuals.
- Use variables to improve performance and troubleshooting.
- Improve performance by reducing cardinality levels.
- Optimize DirectQuery models with table level storage.
- Create and manage aggregations.

# Review performance of measures, relationships, and visuals
## Identify report performance bottlenecks
- slowest query in semantic model 
## Analyze performance
- performance analyzer to check report element performance on interaction.
  - open view ribbon --> performance analyzer 
- clear visual cache by add blank page --> open blank page --> save and close file --> reopen
- data engine cache
  - restart pbi desktop
  - connect dax studio to semantic model and clear cache. 

## review result
performance analyzer
- DAX query: analysis service
- visual display: web image retrieval/geocoding/render
- other:
  - other background task
  - wait for other visual to complete
    - reduce visual in report.

## Resolve issues and optimize performance

### visuals:
- reduce visuals with drill through and tool tips

### dax query:
- starting point is any query longer than 120 ms
- use DAX Studio to investigate your queries in more detail.

### Semantic model:
Instead, if the DAX query is displaying a high duration value, it is likely that a measure is written poorly or an issue has occurred with the semantic model. 

### Relationships
e.g. ensure 1:m is recognized as 1:m

### Columns
remove unnecessary columns:
- what if it is a relationship (id) column required by global semantic model?

### Metadata
- data from power query profiling is considered meta

### auto date/time feature
- turn it off
  - by default pbi create a hidden calc table for each date column
- file --> options and settings --> options --> global/current file --> date load --> time intelligence

# Use variables to improve performance and troubleshooting
- Improved performance
  - reduce repeat calc 
- Improved readability
  - reduces nested hell
- Simplified debugging
  - troubleshoot mulistep by calling return on those var
- Reduced complexity
  - avoids complex functions like `earlier/earliest`
    - seems to be able to be replaced with window function in dax?

# Reduce cardinality

## Identify cardinality levels in columns
- distinct value count
- unique value count

## Reduce relationship cardinality
- Cardinality is the direction of the relationship
- relationship has to be between col of same data type

## Improve performance by reducing cardinality levels
Most effective technique to reduce a model size:
- use a summary table from the data source. 
- Where a detail table might contain every transaction, a summary table would contain one record per day, per week, or per month. It might be an average of all of the transactions per day, for instance.

- An effective technique to reduce the model size is to set the Storage Mode property for larger fact-type tables to DirectQuery. 
  - doesnt work for more than 1 Million rows.

# Optimize DirectQuery models with table level storage

how to work around the 1 million row limit while also be more performant?

if the need to export more than 1 million row is inevitable, is it impossible to do with direct query? is it possible to have a slice and dice always less than 1 mil and return a meaningful message?

- It is suitable in cases where data changes frequently and near real-time reporting is required.
- It can handle large data without the need to pre-aggregate.
- It applies data sovereignty restrictions to comply with legal requirements.
- It can be used with a multidimensional data source that contains measures such as SAP Business Warehouse (BW).

limitation include:
- performance
- security
- data transformation
- modeling
- reporting

## optimize performance

### Optimize data in Power BI Desktop

### Optimize the underlying data source (connected database)
- avoid complex calc column, do it in the source instead.
- review indexes

### Customize the Query reduction options
File > Options and settings > Options > Query reduction
- Reduce number of queries sent by
  - disable visual interaction on default
- slicers 
  - add an apply button VS instant apply change
- FILTERS 
  - add an apply button VS instant apply change

# Create and manage aggregations
The smaller cache size reduces the refresh time, so data gets to users faster.


large semantic model, aggregations can help you reduce and maintain the size of your model.

# Knowledge:
1. What benefit do you get from analyzing the metadata? 
> The benefit of analyzing the metadata is that you can clearly identify data inconsistences with your semantic model.