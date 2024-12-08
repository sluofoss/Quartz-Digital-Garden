---
title: Holiday Destination Flight Recommendation and EDA
created: 2024-11-10
updated: 2024-12-09T00:10
---

# website idea

- use flightradar api for in out flight data

- flight price api to determine/highlight cheap destinations

[reddit recommended rapidapis](https://www.reddit.com/r/datasets/comments/blubr1/is_there_currently_a_free_and_unlimited_api_to/)


# solution architecture 

1. free soln, using aws lambda to crawl data, feed into some data store,  
2. use dbt to transform feed into store / fixated view using athena
	1. the export data store in public s3 bucket will be place behind CDN/API Gateway to rate limit public access.
	2. https://stackoverflow.com/questions/53703781/how-can-i-rate-limit-aws-s3-bucket-access
3. point hosted power bi /plotly dashboard to store
	1. power bi free account should be able to publish to web from inside the default My Workspaces