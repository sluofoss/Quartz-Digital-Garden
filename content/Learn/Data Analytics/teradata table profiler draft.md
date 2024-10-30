---
created: 2024-10-31T01:45
updated: 2024-10-31T01:48
---

```sql
DROP TABLE __MYDATABASE__.__MY_COLUMN_AGG__;
CREATE MULTISET TABLE __MYDATABASE__.__MY_COLUMN_AGG__(
        aggregated_statistic NUMERIC(15,3),
        statistic_type VARCHAR(50),
        columnname VARCHAR(50),
        databasename VARCHAR(50),
        tablename VARCHAR(50)
);
DELETE FROM __MYDATABASE__.__MY_COLUMN_AGG__;

SELECT * 
FROM __MYDATABASE__.__MY_COLUMN_AGG__
ORDER BY  databasename, tablename, columnname, statistic_type

WITH column_clauses AS (
    SELECT 
        C.DatabaseName
        , C.TableName
        , C.columnName
        , (dense_rank() OVER (PARTITION BY C.DatabaseName, c.tablename ORDER BY c.columnname)-1)/30 AS query_group
        --, (dense_rank() OVER (PARTITION BY C.DatabaseName, tablename ORDER BY columnname)-1)/50 AS row_entry
        --, every row should correspond to a column in the table of interest
        , 'crdnl__' || c.columnname AS __car_name
        , 'ntnl__' || c.columnname AS __not_name
        , ', count(distinct t.' || c.columnname || ') as ' || __car_name  AS cardinal_clause
        , ', count( t.' || c.columnname || ') as ' || __not_name  AS not_null_clause 
        , (' union all select ' || __car_name ||  ' as ags, ''crdnl'' as stt, ') || 
          --(C.DatabaseName || ' as databasename, ') ||
          --(C.tablename    || ' as tablename, ') ||
          ('''' || C.ColumnName   || ''' as cnm ') ||
          ' from tv' AS cardinal__union
          --(' from ' || c.databasename || '.' || c.tablename || ' as t;') AS cardinal__union
        , (' union all select ' || __not_name ||  ' as ags, ''ntnl'' as stt, ') || 
          --('''' || C.DatabaseName || ''' as databasename, ') ||
          --('''' || C.tablename    || ''' as tablename, ') ||
          ('''' || C.ColumnName   || ''' as cnm ') ||
           ' from tv' AS not_null__union
    FROM DBC.ColumnsV AS C
    
    -- parameter
    WHERE C.DatabaseName = 'EPCurtdV'
    AND C.TableName IN (
		'__TABLE_OF_INTEREST__'
    )
)
, qrys as (
SELECT 
    c.databasename, C.TableName, c.query_group
    --, 'select ''' || c.tablename || ''' as TableName ' || xmlagg(cardinality_clause || not_null_clause) (VARCHAR(20000)) || ' from ' || databasename || '.' || tablename || ';' AS all_aggs_clauses
    --, 'select ''' || c.databasename || ''' as databasename, ''' || c.tablename || ''' as TableName ' || ( xmlagg(cardinality_clause || not_null_clause) (VARCHAR(20000)) ) || ' from ' || databasename || '.' || tablename || ' as t;' 
    , 'insert into __MYDATABASE__.__MY_COLUMN_AGG__ (aggregated_statistic, statistic_type, columnname, databasename, tablename) ' || 
        'with tv as (select ''' || 
        (c.databasename || ''' as databasename, ''') || 
        (c.tablename || ''' as TableName ') ||
        ( xmlagg(c.cardinal_clause || c.not_null_clause) (VARCHAR(10000)) ) ||
        (' from ' || c.databasename || '.' || c.tablename || ' as t)')
    AS all_aggs_as_col
    , ', header as ( select CAST(-1 AS NUMERIC(15,3)) as ags, ' ||
        'CAST(''_'' AS VARCHAR(50)) as stt, ' ||
        --'CAST(''_'' AS VARCHAR(50)) as databasename, ' ||
        --'CAST(''_'' AS VARCHAR(50)) as tablename, ' ||
        'CAST(''_'' AS VARCHAR(50)) as cnm'  ||
       '), row_to_col as ( select ags, stt, cnm from header' ||
        ( xmlagg(c.cardinal__union || c.not_null__union) (VARCHAR(15000)) ) || ') ' ||
        'select * from row_to_col as d left join (select distinct databasename, tablename from tv) as m on 1 = 1;'
        --(' from ' || c.databasename || '.' || c.tablename || ' as t;')
    AS all_aggs_as_row
    , (all_aggs_as_col || all_aggs_as_row) (varchar(25000)) as exec_query
    , length(all_aggs_as_col) AS query_length_col
    , length(all_aggs_as_row) as query_length_row
    , length(exec_query) AS query_length_exec
FROM column_clauses c
GROUP BY databasename, C.TableName, c.query_group
)
--select max(query_length_col), max(query_length_row), max(query_length_exec)

SELECT *
FROM qrys c
ORDER BY c.databasename, C.TableName, c.query_group
```
