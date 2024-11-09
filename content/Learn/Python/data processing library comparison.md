---
title: data processing library comparison
created: 2024-09-30T21:35
updated: 2024-11-06T00:23
---


1. single node
	1. #polars
	2. #duckdb
	3. #pandas
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