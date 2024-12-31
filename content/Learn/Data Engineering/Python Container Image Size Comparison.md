---
created: 2024-12-31T13:44
updated: 2025-01-01T04:34
title: Python Container Image Size Comparison
tags: 
---
# Abstract


# Motive

#aws Lambda, and thus by assumption Azure Function, and GCP Function environment are not easily, if at all, reproducible during local development. 

Recently for a personal python project, after setting up a new development environment the packaged lambda layer now experiences new issues related to segmentation fault. The code is locally runnable and partially runnable in AWS. However, function calls related to boto3 and s3fs (suspected) causes segmentation fault. 

This lead to the search for deployment method that is still **cheap** (lambda have always free tier), whilst maintaining **environment reproducibility**.

# Exploration

## Deployment via container
- All 3 major platform supports deployment of lambda/functions via containers. 
	- https://cloud.google.com/functions/docs/building
	- https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-container-registry?tabs=acr%2Cbash&pivots=programming-language-csharp
	- https://docs.aws.amazon.com/lambda/latest/dg/python-image.html
### Caveat
- Since container come at the extra cost of storing system information (Linux setups). They would always be larger to deploy. The question is by how much, and whether we can still stay in the free tier?

### Size Comparison
#### Limit on #aws Platform
##### lambda 
Python application packaging is known to be bloated compare to other languages. For the personal project the layer easily reached 70 MB zipped, 184 MB unzipped. So this is already close to the limit. 
> [!NOTE]
> At this time I also have kept boto3 which should be redundant as lambda should have boto3 by default. But I included it to debug segmentation fault, Below is the respective top package size obtained using `du -hs * | sort -hr` inside the `packages` installation folder. Pip Option `--compile` made no difference.

| Size | Lib         |
| :--- | :---------- |
| 65M  | pandas      |
| 41M  | numpy       |
| 26M  | botocore    |
| 25M  | numpy.libs  |
| 12M  | lxml        |
| 7.5M | fastparquet |
| 6.4M | aiohttp     |
| 5.3M | cramjam     |
| 2.8M | tzdata      |
| 2.8M | pytz        |
| 2.7M | yaml        |
| 1.2M | bs4         |
| 1.5M | fsspec      |
| 1.1M | html5lib    |
| 1.1M | yarl        |

> [!TIP]
> For more tips  on how to reduce the size of deployment artifact, see https://towardsdatascience.com/how-to-shrink-numpy-scipy-pandas-and-matplotlib-for-your-data-product-4ec8d7e86ee4

Also, lambda has no GPU options (not that one should run cost intensive application on lambda anyway). So the concern of installing 2 GB GB of Pytorch or tensorflow is an null-issue.

> You can add up to five layers to a Lambda function. The total unzipped size of the function and all layers cannot exceed the unzipped deployment package size quota of 250 MB.

##### #docker container image

According to AWS Official Documentation
> Lambda supports a maximum uncompressed image size of 10 GB, including all layers.

> To make the image compatible with Lambda, you must include a runtime interface client for your language in the image. (non aws images)
> `pip install awslambdaric`

Note that smaller the image, the more likely one runs into compatibility issues. The below table will serve as a comparison of artifact size for python 3.12 on my personal project.

| base image                        | base size | pip install size          | notes|
| :-------------------------------- | :-------- | :------------------------ | :-----------------------|
| public.ecr.aws/lambda/python:3.12 | 532 MB    | 258 + 342 MB (prod + dev) | default aws python image                             |
| python:3.12                       | 1.01 GB   | ?                         | debian based |
| python:3.12-slim                  | 123 MB    |?   | does not contain a lot of defacto debian packages |
| python:3.12-alpine                | 48 MB     | ?                         | smallest with near zero additional toolings like git. in 2020 it was said to pip install from wheel 50x longer, but no longer the case with alpine specific wheels. [forum source ](https://news.ycombinator.com/item?id=38798233) |


> [!NOTE]
> when time permits lets also consider uv images for a dev workflow that does all the following:
> 	- deploy as container
> 	- deploy as package
> 	- packaging and publishing to pypi
> https://docs.astral.sh/uv/guides/integration/docker/
> 
> `uv` images have tags for flavourless, debian and alpine.

> [!TIP] more reading on lightweight python deployment
- https://stackoverflow.com/questions/69560808/how-to-build-a-custom-image-using-pythonalpine-for-use-with-aws-lambda
- https://stackoverflow.com/questions/74211215/workflow-for-building-python-wheels-in-a-multistage-dockerfile-with-pipenv
- https://stackoverflow.com/questions/58300046/how-to-make-lightweight-docker-image-for-python-app-with-pipenv


## Container Image Registry Hosting

### #aws

ECR has a free tier of 50 GB for public image repo but not for private. Hence not suitable for enterprise usage. Also AWS Lambda can only pull from private repo, so the cost is unavoidable outside of 12 month free tier. 
> https://www.reddit.com/r/aws/comments/1358jqy/lambda_docker_with_public_ecr/

Plain storage cost of s3 (standard) vs ecr seems to be about 1:4 (without considering inter service transfer cost) at $0.1/GB for ECR.

For s3 (infrequent) vs ecr cost ratio would be 1:7.

However with request taken into account (constantly updating images) ecr seems better for development stage and large scale multi service deployment (cost of using image within lambda and fargate is free) and s3 seems better for backup.


### other options outside of cloud and lambda context
https://gist.github.com/JakubOboza/fbd6259f5b6321f17e8c3cdb1b095004
