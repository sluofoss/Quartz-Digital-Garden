---
title: Polars
created: 2024-11-16
updated: 2024-11-16

---
# Use case
## using Polars to develop spark udf instead of pandas

> Actually you can. For example, you can use Polars to write Arrow UDF, because Polars allows zero-copy creation of their dataframe from pyarrow RecordBatch and back.
> At the moment there is only `mapInArrow`, but `applyInArrow` is already added to the master branch of PySpark and it will be available in spark 4.0.
> https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInArrow.html
> Polars UDF will be much much faster than pandas UDFs, I already tried it, it gave about x1.5 - x2

[reddit source](https://www.reddit.com/r/dataengineering/comments/1ehbgfl/comment/lfyr3dz/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

# detail tutorial on best way to use polars 
https://kevinheavey.github.io/modern-polars/tidy.html#pivot-and-melt