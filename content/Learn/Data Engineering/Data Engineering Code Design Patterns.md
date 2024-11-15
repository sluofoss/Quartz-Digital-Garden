---
title: Data Engineering Code Design Patterns 
created: 2024-11-10
updated: 2024-11-10
tags:
    - data-engineering
    - design-patterns
---

# source from reddit discussion 
-  https://www.reddit.com/r/dataengineering/comments/wdzyhr/code_design_patterns_for_data_pipelines/

- #idempotence and #determinism. Make sure the pipeline produces the same results for every execution date that it is triggered.

- #idempotence: you dont get duplicates, you get exactly the same set of data, doesnt matter how many times you run it.

- #determinism: you can preddict the transformation output

- Writing self repairing and self backfilling pipelines. They break #idempotence but are simpler to operate in my experience.

- #idempotent, #atomic, and #determinism 

- #singleton is already provided by #pyspark

- But #factory pattern will do charm and reduces efforts. 

# General OOP design patterns

- https://refactoring.guru/design-patterns/catalog

- here we list 3 major categories of design patterns:
    - creational
        - factory
        - abstract factory
        - builder
        - prototype
        - singleton
    - structural
        - adapter
        - bridge
        - composite
        - decorator
        - facade
        - flyweight
        - proxy
    - behavioural
        - chain of responsibility
        - command 
        - iterator
        - mediator
        - mememto
        - observer
        - state
        - strategy
        - template
        - visitor

## speculations
- creational seems to be more on the architectural side of things for #data-engineering?

- structoral should be helpful in developing individual components of pipeline

- behavioural should be helpful in tieing different building blocks of pipeline together.
