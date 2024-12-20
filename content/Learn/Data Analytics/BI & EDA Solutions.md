---
title: BI & EDA Solutions
created: 2024-10-17T00:49
updated: 2024-11-17T23:56
tags:
  - data-analytics
  - eda
---

# FOSS with SAAS
- #metabase
	- toy self serve
		- deploy using single #docker container, #jar
- #apache-superset
	- toy self serve
		- deploy using #docker-compose, #k8s
- #grafana
	- toy self serve
		- deploy using #docker-compose, #k8s
	- pro
		- dashboard can be exported and versioned as json
		- primary use case is system time series telemetry
	- con
		- cross version json compatibility is a joke  
- redash
- kanaries rath
- #KanariesPyGWalker
	- allows tableau eda experience inside Jupyter notebook
- bare-metal self serve
	- #plotly + #Dash + #dbt for semantic layer
		- still uses pandas as final layer for plotting https://plotly.com/blog/polars-to-build-fast-dash-apps-for-large-datasets/
		- but nothing stopping using polars to do heavy data wrangling prior to convert to pandas for final plot.
	- #bokeh + #streamlit + #dbt
	- bokeh seems somewhat limited to python whereas plotly is more widely adopted, go 
# Proprietary
- #Qlik
- #tableau
# Proprietary that gets stuffed down everyone's throat
- #powerbi

# Comparison
## 🖊 TODO
- [ ] refactor below into table
## Interesting stuff that #powerbi #tableau cant do, but come with [[Dash]]
- user edited table ( this allows form entry and calculator style interface).
- some custom visual exists in #powerbi appsource or marketplace but are all proprietory and paid.
  - Most likely require power platform (power app and dataflow as well)
- can be achieved with power app, but power app workflow free tier has 750 limit.
  - described as write back by powerbi and tableau
