# 0x15. API 🖨️
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Learning Objectives
### General
- 📖 What Bash scripting should not be used for
- 📖 What is an API
- 📖 What is a REST API
- 📖 What are microservices
- 📖 What is the CSV format
- 📖 What is the JSON format
- 📖 Pythonic Package and module name style
- 📖 Pythonic Class name style
- 📖 Pythonic Variable name style
- 📖 Pythonic Function name style
- 📖 Pythonic Constant name style
- 📖 Significance of CapWords or CamelCase in Python

## Requirements
### General
- 🚩 Allowed editors: `vi`, `vim`, `emacs`
- 🚩 All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- 🚩 All your files should end with a new line
- 🚩 The first line of all your files should be exactly `#!/usr/bin/python3`
- 🚩 __Libraries imported in your Python files must be organized in alphabetical order__
- 🚩 A `README.md` file, at the root of the folder of the project, is mandatory
- 🚩 Your code should use the `PEP 8` style
- 🚩 All your files must be executable
- 🚩 The length of your files will be tested using `wc`
- 🚩 All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- 🚩 You must use [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- 🚩 Your code should not be executed when imported (by using `if __name__ == "__main__":`)

By Estefania Ruiz 🦌 From Holberton School 🪐
