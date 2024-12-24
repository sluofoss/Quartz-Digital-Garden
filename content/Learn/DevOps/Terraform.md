---
created: 2024-12-23T14:49
updated: 2024-12-23T15:02
title: Terraform
tags:
  - iaac
---


# Terraform: up & running by Yevgeniy Brikman notes

## chapter 1 why terraform
- [[DevOps]] is not a job title, it's a set of processes, ideas, techniques.
> [!TIP]
> The goal of DevOps is to make software delivery vastly more efficient.
> 
> CICD 

### 4 core values to devops 
- culture, 
- automation, 
- measurement, 
- sharing 

> [!NOTE]
> This book focus on automation

### Five broad categories of IaC tools:
- Ad hoc scripts
  - e.g.
    - bash script
    - ruby
    - python
  - issues
    - too much freedom in style and method
- Configuration management tools
  - e.g.
    - chef
    - puppet
    - ansible
  - benefit
    - coding convention
    - idempotence:
      - result guaranteed on repetition
    - distribution
- Server templating tools
  - e.g.
    - docker (container)
    - coreos rkt (container)
    - cri-o (container)
    - podman (container)
    - packer (vm) (prod cloud)
    - vagrant (vm) (dev vbox)
  - 1 example of pattern flow :
    1. packer --> aws ami with docker engine, 
    2. deploy ami to cluster of server, 
    3. deploy docker container across that cluster
  > [!TIP] 
  > key component to immutable infrastructure
- Orchestration tools
  - e.g.
    - k8s
    - marathon/mesos 
    - ecs
    - docker swarm
    - nomad 
- Provisioning tools
  - terraform
  - cloud formation
  - openstack heat
  - aws cdk
  - arm template (azure)
  - pulumi

IaC introduces software engineering practices
- self-service
- speed and safety 
- documentation
- version control
- validation
- reuse
- happiness

> [!NOTE] Terraform written in Go.

### Tradeoff comparison with other tools

#### Configuration management versus provisioning
- Differentiation between config and provision may not be clear cut as some config can be done during provisioning and vice versa.
- Common pattern is provision (terraform) + server template (docker)
- Can also do provision (terraform) + config management (ansible)

#### Mutable infrastructure versus immutable infrastructure
- config management tool by default are stateful/mutable
- mutable downside:
  - cumulative history in `prod` that will not be reflected in `dev`
- immutable downside:
  - time intensive to redeploy for trivial change.
  - once disk is running, the disk will cumulate data and config, becoming stateful.
#### Procedural language versus declarative language
terraform, cf, puppet openstack heat, pulumi are declarative
chef and ansible are procedural

procedural downside:
  - does not capture state
  - limits reusability

#### General-purpose language versus domain-specific language

**Advantage of each**
| dsl                      | gpl                                      |
| :----------------------- | :--------------------------------------- |
| easier to learn          | no need to learn anything new            |
| clearer and more concise | bigger ecosystem and more mature tooling |
| more uniform             | more power and functionality (loop, conditional, autotest, code reuse, abstraction, integration with other tools)       | 

#### Master versus masterless
**Master's pro con table**
| advantage                                              | disadvantage |
| :----------------------------------------------------- | :----------- |
| single place to see status                             | extra infra  |
| potential web interface                                | maintenance  |
| continuous run in background to check for config drift | security (connection to client) |


#### Agent versus agentless
- agent is software on server that does the configuration

**Agent's pro con table**

| advantage | disadvantage                                                                                                        |
| :-------- | :------------------------------------------------------------------------------------------------------------------ |
|           | bootstraping (how to orchestrate agent itself in the first place? external dependency or unnatural bootstrap?)      |
|           | maintenance (sync with master and monitor for crash) more moving part is more chance of failure and timely to debug |
|           | security (connection to master)                                                                                     |

#### Paid versus free offering
> [!WARNING] teraform is no longer open source, still free. Consider using open tofu (an open source fork of terraform) as an alternative.
> https://spacelift.io/blog/terraform-license-change#what-is-the-likely-impact-of-the-terraform-bsl-license-change

- pulumi free is said to be not production ready. It needs the paided pulumi backend to support transactional checkpointing for fault tolerance and recovery, concurrent state locking (prevent team overriding causing corruption), encrypt state in transit and at rest

#### Large community versus small community
- to check community size, check 
  - github contributor
  - github star
  - downstream libraries
  - stack overflow questions
  - multi cloud support
  - open or closed source
  - 
#### Mature versus cutting-edge
how stable and old is the tool

#### Use of multiple tools together
**common patterns**
- provisioning + config management
- provisioning + server templating
- provisioning + server templating + orchestration

#### summary:
|              | chef        | Puppet      | Ansible     | Pulumi       | CloudFormation | Heat         | Terraform        | OpenTofu                       |
| :----------- | :---------- | :---------- | :---------- | :----------- | :------------- | :----------- | :--------------- | :----------------------------- |
| Source       | Open        | Open        | Open        | Open         | Closed         | Open         | Source available | Open                           |
| Cloud        | All         | All         | All         | All          | AWS            | All          | All              | All                            |
| Type         | Config mgmt | Config mgmt | Config mgmt | Provisioning | Provisioning   | Provisioning | Provisioning     | Provisioning                   |
| Infra        | Mutable     | Mutable     | Mutable     | Immutable    | Immutable      | Immutable    | Immutable        | Immutable                      |
| Paradigm     | Procedural  | Declarative | Procedural  | Declarative  | Declarative    | Declarative  | Declarative      | Declarative                    |
| Language     | GPL         | DSL         | DSL         | GPL          | DSL            | DSL          | DSL              | DSL                            |
| Master       | Yes         | Yes         | No          | No           | No             | No           | No               | No                             |
| Agent        | Yes         | Yes         | No          | No           | No             | No           | No               | No                             |
| Paid Service | Optional    | Optional    | Optional    | Must-have    | N/A            | N/A          | Optional         | N/A                            |
| Community    | Large       | Large       | Huge        | Small        | Small          | Small        | Huge             | Large (half star as terraform) |
| Maturity     | High        | High        | Medium      | Low          | Medium         | Low          | Medium           | Medium                         |

author from https://www.gruntwork.io/, also now support OpenTofu

## chapter 2 getting started
### [Optional] Tutorial
- setting up aws account
- install terraform (locally)
- deploy single server
- deploy configurable web server
- deploy cluster of web server
- deploy load balancer 
- clean up

### takeaway
- `terraform init` is idempotent, and run everytime looking at new code
- `terraform plan` review proposed change before `apply`

- terraform resource come from providers.
- resource have tags
- resource interdepends and terraform can figure out the dependency and what to build first.
- dependency can be visualized using graphviz


## chapter 3 manage state

## chapter 4 reusable module

## chapter 5 tips and tricks loops, ifs, deploy and gotcha

## chapter 6 managing secrets

## chapter 7 multi providers

## chapter 8 production grade terraform code

## chapter 9 testing terraform code

## chapter 10 use terraform as a team
