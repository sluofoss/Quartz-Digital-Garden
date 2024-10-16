---
created: 2024-09-30T21:35
updated: 2024-10-17T01:01
---

https://duckdb.org/docs/guides/meta/explain_analyze.html


```python
query_str = "pragma enable_profiling; explain analyze select * from df"
duckdb.sql(query_str)
```

the above seems all fine and dandy until you realize that the profiler string formatting is truncated in jupyter notebook.

what you need to do instead is use to python api to get proper output as described here
https://github.com/duckdb/duckdb/issues/13195

```python
query_str = "pragma enable_profiling; select * from df"
duckdb.sql(query_str).explain('analyze')
```

as of 30/09/2024, the aforementioned improvement in docs is not part of official documentation.