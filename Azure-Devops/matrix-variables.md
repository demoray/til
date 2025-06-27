# Using matrix values in conditionals

In order to use [matrix strategies](https://learn.microsoft.com/en-us/azure/devops/pipelines/customize-pipeline?view=azure-devops#build-using-multiple-versions) with [conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops), first define the strategy thusly:

```yaml
strategy:
  matrix:
    a:
      my_variable: true
      python.version: "3.9"
    b:
      my_variable: false
      python.version: "3.10"
```

To use the value `python.version` in a step:

```
  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: "$(python.version)"
```

To use the value `my_variable` as a conditional:

```
  steps:
  - bash: echo "is set"
    condition: eq(variables.my_variable, true))
  - bash: echo "is not set"
    condition: eq(variables.my_variable, false))
```
