# 0x05. Python - Exceptions

## Description

This project explores the concept of exceptions in Python. Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. Understanding and handling exceptions is crucial for writing robust and error-tolerant Python code.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

No special installation steps are required for this project. Simply clone the repository to your local machine.

```bash
git clone https://github.com/your-username/0x05-python-exceptions.git

## Usage
To use the code in this project, import the necessary modules and classes into your own Python scripts. Handle exceptions where necessary to ensure graceful error recovery.

from exceptions_module import CustomException

try:
    # Your code that may raise exceptions
    result = some_function()
except CustomException as ce:
    # Handle custom exception
    print(f"Custom Exception: {ce}")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
else:
    # Code to run if no exceptions were raised
    print("No exceptions occurred.")
finally:
    # Code to run regardless of whether an exception occurred
    print("This will always execute.")

## Examples
Include examples of how to use the code in this project. This section helps users understand the practical application of the provided code.

# Example 1: Using a custom exception
from exceptions_module import CustomException

try:
    # Code that may raise CustomException
    raise CustomException("This is a custom exception.")
except CustomException as ce:
    print(f"Caught CustomException: {ce}")


## Contributing
If you find issues or have improvements to suggest, feel free to contribute. Follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear commit messages.
Push your changes to your fork.
Submit a pull request.

# License
This project is licensed under the MIT License. Feel free to use and modify the code according to the terms of the license.

    Contact : b.koukin@gmail.com 
    Web : https://bkaoukine.github.io/me/
