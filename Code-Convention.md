# Dekutree Python Style Guide

## Table of Contents

- [1. Flake8](#flake8)
- [2. Naming Conventions](#naming-conventions)
  - [2-1. Descriptive Naming](#descriptive-naming)
  - [2-2. camelCase](#descriptive-naming)
  - [2-3. PascalCase](#descriptive-naming)
  - [2-4. snake_case](#descriptive-naming)
- [3. Module](#module)
- [4. Function](#function)

## [1](#flake8) Flake8

- Use flake8 as basic linter.

  - console (usage)

    ```console
    pip install flake8
    flake [option] <file_name|dir_name>  # check file or entire directory
    ```

  - settings.json (setting on vscode)

    ```json
    {
        "python.linting.flake8Enabled" : true,
        "python.linting.pylintEnabled" : false
    }
    ```

## [2](#naming-conventions) Naming Conventions

### [2.1](#descriptive-naming) Descriptive Naming

- Avoid single letter names. Be descriptive with your naming

    ```python
    # bad
    def q():
        # ...

    # good
    def quit():
        # ...
    ```

### [2.2](#camel-case) camelCase

- __fill out camelCase examples__

### [2.3](#pascal-case) PascalCase

- __fill out PascalCase examples__

### [2.4](#snake-case) snake_case

- __fill out snake_case examples__

## [3](#module) Module

- about import?

## [4](#function) Function

- spacing rules etc.
