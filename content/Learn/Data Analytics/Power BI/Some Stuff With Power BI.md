---
created: 2024-10-03T20:59
updated: 2024-11-06T00:07
tags:
  - data-analytics
  - "#powerbi"
---
# pbip
it is possible to create custom DAX and power query import tables by editing the text file model.bim

however it doesnt work for power query direct query mode for teradata for some reason.

# bypass the 1 million row limit from power bi premium

1. import mode/ splitting direct query table using rank filte 
2. use 
	1. var c1 = calculate(table, relatedtable(hugetable))
	2. var c2 = calculate(table, relatedtable(hugetable))
	3. var c3 = calculate(table, relatedtable(hugetable))
	4. return union(c1, c2, c3)

you can query cube (ssas) using dax nested within  m query, in m query you can have loop, thus it should be able to get around that. but have been hitting alot of server side error.


# power bi user defined aggregation

- it should act as a replacement table for fact connecting to the corresponding dimensions (based on the same connecting key)
- it only becomes active when the dimension table are set to dual mode (this way it doesnt perform direct query). As long as dimension table is direct query and not dual, it doesn't use the user defined aggregation.

[User-defined aggregations - Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/aggregations-advanced)


# dax performance
[Solved: Better Performance with TREATAS - Microsoft Fabric Community](https://community.fabric.microsoft.com/t5/Desktop/Better-Performance-with-TREATAS/td-p/3696907)

Mdx vs dax  


# some QA with semantic model storage
1. is power bi semantic model stored tabular or a cube? 
	1. TABULAR 
2. in AnalysisService.Database AnalysisServices.Database - PowerQuery M | Microsoft Learn, it says that the query should be MDX, but obviously we're using DAX instead and it works. 
	1. DAX for multidimensional models in SQL Server Analysis Services | Microsoft Learn
	2. Because semantic model is tabular, this is a rabbit hole not worth diving to.
3. MDX is suppose to be for cube data but it also works on tabular? 
	1. DAX vs MDX — Is there any difference? | by Muhammad Asif | Medium
4. does whether it been tabular or cube affect how we can most efficiently query the semantic model in SSAS?
	1. DAX for multidimensional models in SQL Server Analysis Services | Microsoft Learn
	2. Not necessary.