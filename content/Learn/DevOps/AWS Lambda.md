---
created: 2025-01-31T00:56
updated: 2025-01-31T01:02
tags:
  - aws
title: AWS Lambda
---
# Some issues experienced with AWS Lambda

1. problem testing local containerized lambda with lambda runtime emulator
	1. not sure since when but suddenly I cannot trigger curl the container from outside and resulting in weird http0.9 issues. the container does seem to be running on bridge mode and the port is correctly forwarded and reachable. but no result is produced.
	2. given that the curl can be run successfully inside the container. I'll put this into the cloud environment for a trial run to see if it would work there.
2. size of arm64 image is bigger than amd64
	1. not sure yet whether this is coming from extra pip size or base image size
	2. the size difference is 30 MB, this slightly negates the cost benefit of arm64 lambda being cheaper to execute, also, I'm still within the free tier limit. 