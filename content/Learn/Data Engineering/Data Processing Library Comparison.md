---
title: Data Processing Library Comparison
created: 2024-09-30T21:35
updated: 2024-11-16T00:23
---


1. single node
	- [[Polars]]
	- #duckdb
	- #pandas
	
get dummies / select case when
	polars  (5x)< pandas (5x)< duckdb 

dates
	polars (10x) < pandas < ?(syntax too complicated and not automated)

adjoin with [[sklearn]]: 
	one hot encoding: 
		pd sparse < pl sparse < pd < pl

feature engine only supports pandas , not polars

1. distributed
	1. #ray
	2. #dask
	3. #pyspark

[Spark, Dask, and Ray: Choosing the Right Framework (domino.ai)](https://domino.ai/blog/spark-dask-ray-choosing-the-right-framework)


# compatibility layer on top of dataframe libraries:
- #narwhals
	- currently supports pandas, polars, dask. 
	- duckdb, pyspark, ibis on roadmap
	- https://narwhals-dev.github.io/narwhals/roadmap_and_related/


# tabulated comparison

| library  | speed | distributed | api    | sql interface   |
| -------- | ----- | ----------- | ------ | --------------- |
| pandas   | slow  | no          | pandas | pandasql/duckdb |
| polars   | fast  | no          | polars | Y               |
| duckdb   | fast  | no          | duckdb | Y               |
| dask     |       | yes         | pandas | dask-sql        |
| spark    |       | yes         | spark  | spark-sql       |
| narwhals | NA    | NA          | polars | N               |


# narwhals vs ibis for compatibility
> - Ibis provides a Pythonic frontend to various SQL (as well as Polars LazyFrame) engines
> - Ibis supports SQL engines (and can translate to SQL)
> - Narwhals is extremely lightweight and comes with zero required dependencies, Ibis requires pandas and PyArrow for all backends
> - Ibis has no way to get back to the input type exactly
> [comparison to ibis](https://narwhals-dev.github.io/narwhals/roadmap_and_related/#ibis)