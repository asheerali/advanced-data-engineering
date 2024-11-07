# Project Plan

## Title

Traffic Crash Patterns: Assessing the Influence of Human Factors

## Main Questions

1. How do driver characteristics (e.g., age, sex, use of safety equipment) correlate with injury severity in crashes?

2. What are the most common vehicle types and conditions associated with high-severity crashes?

## Description

This data science project aims to investigate factors contributing to traffic incident outcomes, focusing on crash data from Chicago[^r1][^r2]. By analyzing datasets covering vehicle details, occupant characteristics, and crash conditions, the project seeks to identify patterns related to injury severity and common crash profiles. Insights from this analysis could inform urban safety policies and targeted interventions to reduce crash impact.

The study will examine driver demographics, vehicle types, and situational factors (like the time of the incident and the use of safety equipment) to explore correlations with injury outcomes[^r1]. Additionally, vehicle trajectories and types will be analyzed to determine which combinations frequently lead to high-severity incidents[^r2]. The project will leverage statistical analysis and visualization to draw actionable insights.

## Datasources

### Datasource 1: Traffic Crashes - People

- Metadata URL: https://catalog.data.gov/dataset/traffic-crashes-people
- Data URL: https://data.cityofchicago.org/api/views/u6pd-qa9d/rows.csv?accessType=DOWNLOAD
- Data Type: CSV

Contains records of individuals involved in crashes, detailing demographics, safety equipment use, and injury severity.

### Datasource 2: Traffic Crashes - Vehicles

- Description: https://catalog.data.gov/dataset/traffic-crashes-vehicles
- Data URL: https://data.cityofchicago.org/api/views/68nd-jvt3/rows.csv?accessType=DOWNLOAD
- Data Type: CSV

Records of vehicles (or “units”) involved in traffic incidents, including type, direction, and damage details.

## Work Packages

This project is structured into six work packages, represented as [milestones in the GitHub repository](https://github.com/asheerali/advanced-data-engineering/milestones).

1. **Project Definition and Data Source Selection** [[WP1](https://github.com/asheerali/advanced-data-engineering/milestone/1)]
   1. Define the research topic on a given theme.
   2. Define the research question on a selected topic.
   3. Locate potential data sources.
   4. Evaluate the identified data sources.
2. **Data Acquisition and Pipeline** [[WP2](https://github.com/asheerali/advanced_data_engineering/milestone/2)]
   1. Determine the best data storage format.
   2. Data Pipeline.
3. **Data Exploration, Analytics and Report** [[WP3](https://github.com/asheerali/advanced_data_engineering/milestone/3)]
   1. Conduct exploratory data analysis and preliminary visualization.
   2. Create DataLoader, Pipeline, Visualizations, Models, etc.
   3. Address all the research questions.
   4. Draw conclusions form the analysis.
4. **Automated Testing** [[WP4](https://github.com/asheerali/advanced_data_engineering/milestone/4)]
   1. Create Tests.
5. **Continuous integration** [[WP5](https://github.com/asheerali/advanced_data_engineering/milestone/5)]
   1. Develop CI.
   2. Develop CI for Pre-Commit.
6. **Final Report** [[WP6](https://github.com/asheerali/advanced_data_engineering/milestone/6)]
   1. Develop visual representations.
   2. Enhance the repository's presentation.
   3. Prepare the final presentation.

Work packages must be completed sequentially as each one depends on the completion of all preceding ones.

## References and footnotes

[^r1]: https://catalog.data.gov/dataset/traffic-crashes-people
[^r2]: https://catalog.data.gov/dataset/traffic-crashes-vehicles
