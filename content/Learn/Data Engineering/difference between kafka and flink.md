---
title: difference between kafka and flink
created: 2024-10-03T00:53
updated: 2024-10-17T20:54
tags:
  - data-engineering
---

https://www.reddit.com/r/apachekafka/comments/1d9q6ss/comment/l7gc7an/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

[NoPercentage6144](https://www.reddit.com/user/NoPercentage6144/)
```
I think your question is getting to the heart of the discussion - Flink and Kafka Streams are built for different personas. Kafka Streams and Flink can both process at a scale that most companies are unlikely to ever reach, that's not likely to be the main differentiator for you.

If you're a developer writing a realtime application, Kafka Streams is deployed just like you would deploy any other app. It works with your monitoring, CI/CD, alerting, etc... and you don't need to manage anything centralized. This works quite well for developers.

OTOH, Flink works particularly well if you have a centralized team (or a company like Confluent manage it for you, but there are other tradeoffs there) that is in charge of operations. This allows you to centralize expertise and have one team provide an SLA for all stream processing jobs at your company. This works much better for the "data science" persona.

This article is pretty old, but does a really good job explaining the differences: [https://www.confluent.io/blog/apache-flink-apache-kafka-streams-comparison-guideline-users/](https://www.confluent.io/blog/apache-flink-apache-kafka-streams-comparison-guideline-users/) and this whitepaper covers it in a bit more depth (but you need to give an email to access it): [https://www.responsive.dev/resources/foundations-whitepaper](https://www.responsive.dev/resources/foundations-whitepaper)
```
