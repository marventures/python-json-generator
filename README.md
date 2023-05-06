# Python JSON Generator

This is a Python JSON Generator created using Python File Handling, Python Exceptions and Python Modules.

## Table of contents

- [Overview](#overview)
  - [How to use the project](#how-to-use-the-project)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### How to use the project

#### Step 1: Setting up Initial Requirements:

1. Python 3.11 and above — Follow [this link](https://www.python.org/downloads/) to download Python for your operating system. You can refer to these tutorials on YouTube for the same — Windows, Mac-OS, Ubuntu (it’ll be somewhat similar for other Linux distributions).

2. pip — pip has been included with the Python installer since versions 3.4 for Python 3 and 2.7.

3. Install pipenv using pip — pip install pipenv

#### Step 2: Setting up Python Virtual Environment using pipenv:

1. Install required dependencies using pipenv — pipenv install
2. Activate Python Virtual Environment — pipenv shell
3. Run the program — python main.py

### Screenshot

### Links

- Github: [Code](https://github.com/marvedventures/python-json-generator)

## My process

### Built with

- [Python](https://www.python.org/) - python.org
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Python Virtual Environment.

### What I learned

- Python Exceptions
- Try/ Except Statements
- Python File Handling
- Creating and Reading Files in Python
- Accessing Modules
- Writing Import Statements

  Here is a code snippet:

```py
import json
from input_module import get_employee_details


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            employee_list = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        employee_list = []
    return employee_list


def write_json_to_file(json_obj, output_file):
    with open(output_file, 'w') as f:
        json.dump(json_obj, f, indent=4)


def main():
    file_path = './employees.json'
    employee_list = read_json_file(file_path)

    while True:
        employee_dict = get_employee_details()
        employee_list.append(employee_dict)

        choice = input(
            "Do you want to enter details for another employee? (Y/N): ")
        if choice.lower() == 'n':
            break

    write_json_to_file(employee_list, file_path)


if __name__ == '__main__':
    main()

```

### Useful resources

- [Python File Handling](https://www.geeksforgeeks.org/file-handling-python/) - This helped me understand the concept of File Handling in Python.
- [Python Exceptions](https://www.tutorialspoint.com/python/python_exceptions.htm) - This helped me understand the use Python Exceptions.
- [Pipenv Setup](https://python.plainenglish.io/setting-up-a-basic-django-project-with-pipenv-7c58fa2ec631) - This helped me setup my python virtual env

## Author

- Website - [Marvin Morales Pacis](https://marvin-morales-pacis.vercel.app/)
- LinkedIn - [@marvedventures](https://www.linkedin.com/in/marvedventures/)
- Twitter - [@marvedventures](https://www.twitter.com/marvedventures)
