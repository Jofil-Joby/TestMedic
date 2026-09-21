## Decision and Reasoning

TestMedic decides whether a project has recognizable automated-test evidence. It flags a missing test surface when no test- or spec-like file is detected, then connects that observation to a practical testing improvement.

## Inputs and Data Sources

It uses the inspected project file list and readable source content as its primary evidence. The decision is driven by explicit diagnostic rules rather than an assumed coverage percentage.

## Limits and Constraints

It cannot prove that a project is fully tested, nor can absence of a recognizable test filename prove that tests do not exist. Generated tests, external test suites, and nonstandard naming may require manual review.
