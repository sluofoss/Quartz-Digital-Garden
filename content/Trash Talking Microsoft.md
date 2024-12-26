---
title: Trash Talking Microsoft
created: 2024-12-26
updated: 2024-12-26

---

# The Data Engineering Predicament
Microsoft's data engineering products have become a particular pain point. As discussed in various technical communities, including a notable thread on r/dataengineering, their offerings often feel like a "merry-go-round of mediocrity." The SaaS support is particularly problematic, leaving many enterprises struggling with basic integration issues.
# Reliability Concerns
One of the most frustrating aspects of the Microsoft ecosystem is the frequency of Azure system outages. Unlike traditional on-premise solutions or competing cloud providers, these outages are increasingly viewed as a normal occurrence rather than exceptional events. This "new normal" is simply unacceptable for businesses requiring high availability.
# The Abandonment Pattern
Microsoft has developed a concerning pattern of vendor lock-in followed by product abandonment. Consider these examples:

- VB6, once a cornerstone of business application development
- Windows Mail and Calendar
- Windows Subsystem for Android (WSA)
- The entire Lumia mobile ecosystem
- Various UI frameworks including WPF, MFC, Win32, Windows Forms, and Windows RT

This history makes it difficult to trust long-term investment in new Microsoft technologies.

# Complexity Over Simplicity
Microsoft consistently ignores the "worse is better" philosophy that has proven successful in system design. This principle, which favors simplicity and practicality over complex completeness, seems foreign to Microsoft's development approach. Compare:

- PowerShell's complexity versus Bash's simplicity
- DAX's convoluted syntax versus standard SQL

An example of this principle outside of Microsoft is the XML versus JSON scenario. the fact that XML is more syntactically comprehensive and self describing. It doesn't make it efficient to use in production.

# The Control Problem
The fundamental difference between Microsoft's approach and open systems like Linux becomes apparent in troubleshooting scenarios. With Linux, you can investigate issues, roll back changes, and implement fixes independently. In contrast, Microsoft's systems often leave you at their mercy - particularly during mandatory updates that can bring services down with no clear resolution timeline.
# Documentation and Interface Chaos
Microsoft's documentation strategy creates additional challenges:

- Constant interface updates that invalidate existing documentation
- Over-reliance on GUI-based solutions that change frequently
- Unnecessary complications of simple concepts (like the namespace pollution of curl and wget in PowerShell)
- Preference for complex graphical interfaces over simple, efficient text-based solutions

The most frustrating aspect is that these changes don't always represent improvements - sometimes they actively make things worse while breaking existing workflows.
# Conclusion
While Microsoft's products remain central to many organizations' operations, their approach to software development and ecosystem management raises serious concerns. The combination of vendor lock-in, frequent abandonment of technologies, overcomplexification, and reliability issues creates an environment that's increasingly difficult to justify from both technical and business perspectives.
As developers and system architects, we need to carefully consider these factors when making technology choices. Sometimes, the seemingly more complex path of open systems ultimately provides more stability, control, and long-term viability than Microsoft's supposedly integrated solutions.
