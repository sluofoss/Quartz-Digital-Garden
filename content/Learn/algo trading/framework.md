---
title: algo trading framework
created: 2024-10-05T15:17
updated: 2024-10-10T00:03
draft: "true"
---

https://pipekit.io/blog/python-backtesting-frameworks-six-options-to-consider

- backtrader has access to both live feed from IB and yahoo finance, 

# steps

- find wins
- list all previous time series within time frame
- calculate all possible features
- see if there are any bunch of time series that show visible clusters
- for all clusters 
	- extract pattern (may be manual)
- for all pattern
	- find occurrence in full dataset
	- see ratio of pattern consequent win vs loss 
	- this should locate good patterns
- select patterns that 
	- occurs NOT rarely
	- have good ratio of wins vs loss above 7:3 or 9:1
	- 