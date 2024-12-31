---
title: AWS Networking
created: 2024-12-24
updated: 2024-12-31T15:17
tags:
  - aws
---

#TODO

# VPC
https://repost.aws/questions/QUK_vSmINHSXCC8oVwe3DVsA/aws-theory-why-an-ec2-need-a-vpc
https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html

default vpc are all public subnets, i.e. accessible from public internet
# Subnet

# CIDR
https://medium.com/@hildamachando4/cidr-blocks-in-aws-understanding-the-basics-and-beyond-f74506a84b83


# Open Systems Interconnection (OSI)

# load balancer terraform resource required
the diagram indicates what resource mentions what resource
```mermaid
graph LR
aws_lb_listener --> aws_lb --> aws_security_group 
aws_lb --> data.aws_subnets
aws_lb_target_group --> data.aws_vpc
aws_autoscaling_group --> data.aws_subnets
aws_autoscaling_group --> aws_lb_target_group
%%aws_lb_listener --> aws_lb_target_group
aws_lb_listener_rule --> aws_lb_listener
aws_lb_listener_rule --> aws_lb_target_group
```

# other 
> [!NOTE]
> by default all aws resources, including alb dont allow income or outgoing traffic, so they need security group definition.
