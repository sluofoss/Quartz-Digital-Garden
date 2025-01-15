---
title: 3 create interactive report with copilot
created: 2025-01-02T14:41
updated: 2025-01-02T16:34
---
Copilot for Power BI can perform certain tasks, such as:

- Create measures based on natural language.
- Update the semantic model with synonyms for improved user Q&A experience.
- Generate report content, summary visuals, and pages from prepopulated prompts.
- Analyze a summary of underlying semantic model.

only works when model is of good data quality
- **Completeness**: Missing values can cause gaps.
- **Validity**: Out-of-range data values can skew visuals and results.
- **Consistency**: Inconsistent data can affect date-related visuals.
- **Uniqueness**: Duplicates can affect data accuracy.
- **Data Relationships**: Cross-table visuals might not be possible without relationships.
- **DAX Calculations**: Limited calculations can result in fewer possible insights.
Use Power Query to ensure data quality:

- **Profile your data** by assessing column quality, distribution, and profile.
- **Clean your data** by resolving inconsistencies, unexpected or null values, and other data quality concerns.
- **Transform your data** by implementing user-friendly naming conventions for columns and queries, altering column data types, and applying data shape transformations.

> ![NOTE]
> You need to have write access to a workspace that is on F64 or Power BI Premium in the Power BI service, where you plan to publish the report. Learn how to [Enable Copilot for Power BI](https://learn.microsoft.com/en-us/fabric/get-started/copilot-enable-fabric).

## model data
Star or snowflake schema

create quick measures (suggest by copilot)

also ask copilot to suggest measures

## Create reports with Copilot for Power BI
you can ask copilot to create a new report page by clicking the copilot button/ pane.
the prompt can also be customized

## Create summaries with Copilot for Power BI
The Narrative visual allows you to create a custom visual that summarizes and references data within your report visuals. Custom narratives give more control over formatting and text. Copilot created summaries include the following suggested prompts:

- _Give an executive summary_
- _Answer likely questions from leadership_
- _Create a bulleted list of insights_

## what Microsoft considers as "correct" answer
What is the purpose of creating relationships between tables in Power BI?

- To filter and summarize data in report visuals.

Correct. Relationships between tables allow for filtering and summarizing of data in report visuals.

- To create a more visually appealing data model.

- To reduce the amount of data stored in each table.

Incorrect. Relationships do not reduce the amount of data stored, but rather allow for more efficient analysis of the data.
(bullshit, star schema by default make storage more efficient by reducing repetitiveness)