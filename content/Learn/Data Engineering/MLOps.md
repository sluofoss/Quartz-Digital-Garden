---
title: MLOps
created: 2024-11-05T22:50
updated: 2024-11-10T00:30
tags:
  - data-engineering
---

# stack
https://www.reddit.com/r/mlops/comments/1ephb1p/whats_your_mlops_stack/

https://ml-ops.org/content/state-of-mlops

https://docs.databricks.com/en/machine-learning/mlops/mlops-stacks.html

https://github.com/kelvins/awesome-mlops


# using #dbt + #feast + #teradata
This article explains how feast is used: simplifying and standardizing the retrieval of a training dataset for cross project management.
https://developers.teradata.com/quickstarts/manage-data/getting-started-dbt-feast-teradata-pipeline/

# interested compatible FOSS stack components

| type                                | tool                                  |
| ----------------------------------- | ------------------------------------- |
| data source                         | #spark #kafka #pulsar #api #warehouse #postgresql |
| data source transform orchestration | #dbt #sqlmesh                         |
| data source/model catalog           | #datahub #amundsen-io #OpenMetadata   |
| feature store/share/documentation   | #feast                                |
| model build/train                   | [[sklearn]], #spark, #xgboost #ray    |
| model code dev                      | #mlflow                               |
| model registry                      | #mlflow                               |
| model serve                         | #kubeflow                             |
| model orchestration                 | #airflow, #argoflow                   |
| IaC                                 | #terraform                            |
| CICD                                | #github #gitlab workflow |
| Monitor                             | #prometheus #grafana                  |

# lineage visibility:

#datahub supports sourcing lineage from the following:

- majority of data sources listed above
- feature store #feast
- model registry #mlflow
- model orchestration #airflow

# integration with dominating stack
- #ray + #mlflow + #databricks 
	- https://docs.databricks.com/en/machine-learning/ray/ray-mlflow.html