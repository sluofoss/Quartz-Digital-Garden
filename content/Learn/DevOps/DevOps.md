---
title: DevOps
created: 2024-12-23
updated: 2025-01-01T15:09
---

> [!WARNING]
> this page is base on claude.ai result


# #data-engineering + DevOps

DevOps practices are crucial for data engineers, who need to build and maintain reliable data pipelines and infrastructure
Key areas include:

- CI/CD for data pipelines and ETL processes
- Infrastructure as Code (IaC) for data storage and processing systems
- Automated testing of data quality and pipeline functionality
- Monitoring and alerting for data flows and system health
- Version control for data schemas, pipeline code, and configurations



# #data-science + DevOps (sometimes called " [[MLOps]] ")

[[MLOps]] is a specialized case of devops where the principal is the same but infrastructure differs somewhat from devops in software development.

Focuses on operationalizing machine learning models and maintaining reproducible experiments
Key areas include:

- Version control for model code, training data, and hyperparameters
- Automated model training and validation pipelines
- Model deployment and serving infrastructure
- Model performance monitoring and retraining triggers
- Experiment tracking and reproducibility tools
> for more information see
> 
> https://www.phdata.io/blog/mlops-vs-devops-whats-the-difference/
>
> https://www.veritis.com/blog/demystifying-mlops-vs-devops-understanding-the-key-differences/

## TODO
- [ ] aggregate comparison tables from 2 links above here

# #data-analytics + DevOps

Generally has less direct DevOps involvement compared to engineering and science roles
Key areas include:

- Version control for analysis code and dashboards
  - git and pbip for #powerbi
  - azure devops
- Automated report generation and distribution
- Dashboard deployment and maintenance
- Data quality monitoring for analytics datasets
  - monitoring of power bi dashboard meta data
- Access management for analytics tools and data
  - power bi admin portal


# Common DevOps Tools & Practices Across Data Roles:

Version Control: Git for code, DVC for data
Containerization: #docker for consistent environments
Orchestration: #k8s, #airflow for workflows
Infrastructure: [[Terraform]], CloudFormation for provisioning
Monitoring: #prometheus, #grafana for metrics and visualization
CI/CD: #jenkins, GitLab CI for automation

The role of DevOps becomes more critical as data projects move from experimentation to production.