# Importing Private Libraries

There are two ways to use private code within Azure Functions deployed using `func core tools`.

1. Use the [shared\_code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#import-behavior) example from Azure Functions.
2. Package the library as a [wheel](https://pypi.org/project/wheel/) and use requirements.txt to install a module provided via disk.

Example requirements.txt
```
azure-functions~=1.3.0
./mylib-0.0.0-py3-none.any.whl
```
