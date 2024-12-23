---
created: 2024-12-23T14:49
updated: 2024-12-23T15:02
title: Terraform
tags:
  - iaac
---
# Table of Content
- [Table of Content](#table-of-content)
- [Terraform: up \& running by Yevgeniy Brikman notes](#terraform-up--running-by-yevgeniy-brikman-notes)
  - [chapter 1 why terraform](#chapter-1-why-terraform)
    - [4 core values to devops](#4-core-values-to-devops)
    - [Five broad categories of IaC tools:](#five-broad-categories-of-iac-tools)
    - [Tradeoff comparison with other tools](#tradeoff-comparison-with-other-tools)
      - [Configuration management versus provisioning](#configuration-management-versus-provisioning)
      - [Mutable infrastructure versus immutable infrastructure](#mutable-infrastructure-versus-immutable-infrastructure)
      - [Procedural language versus declarative language](#procedural-language-versus-declarative-language)
      - [General-purpose language versus domain-specific language](#general-purpose-language-versus-domain-specific-language)
      - [Master versus masterless](#master-versus-masterless)
      - [Agent versus agentless](#agent-versus-agentless)
      - [Paid versus free offering](#paid-versus-free-offering)
      - [Large community versus small community](#large-community-versus-small-community)
      - [Mature versus cutting-edge](#mature-versus-cutting-edge)
      - [Use of multiple tools together](#use-of-multiple-tools-together)
  - [chapter 2 getting started](#chapter-2-getting-started)
  - [chapter 3 manage state](#chapter-3-manage-state)
  - [chapter 4 reusable module](#chapter-4-reusable-module)
  - [chapter 5 tips and tricks loops, ifs, deploy and gotcha](#chapter-5-tips-and-tricks-loops-ifs-deploy-and-gotcha)
  - [chapter 6 managing secrets](#chapter-6-managing-secrets)
  - [chapter 7 multi providers](#chapter-7-multi-providers)
  - [chapter 8 production grade terraform code](#chapter-8-production-grade-terraform-code)
  - [chapter 9 testing terraform code](#chapter-9-testing-terraform-code)
  - [chapter 10 use terraform as a team](#chapter-10-use-terraform-as-a-team)



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
#### General-purpose language versus domain-specific language
#### Master versus masterless
#### Agent versus agentless
#### Paid versus free offering
> [!WARNING] teraform is no longer open source, still free. Consider using open tofu (an open source fork of terraform) as an alternative


#### Large community versus small community
#### Mature versus cutting-edge
#### Use of multiple tools together

## chapter 2 getting started
- `terraform plan` review proposed change before `deploy`
## chapter 3 manage state

## chapter 4 reusable module

## chapter 5 tips and tricks loops, ifs, deploy and gotcha

## chapter 6 managing secrets

## chapter 7 multi providers

## chapter 8 production grade terraform code

## chapter 9 testing terraform code

## chapter 10 use terraform as a team
