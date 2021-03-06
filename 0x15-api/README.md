# 0x15. API π¨οΈ
Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them β access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so letβs build Python scripts.

## Learning Objectives
### General
- π What Bash scripting should not be used for
- π What is an API
- π What is a REST API
- π What are microservices
- π What is the CSV format
- π What is the JSON format
- π Pythonic Package and module name style
- π Pythonic Class name style
- π Pythonic Variable name style
- π Pythonic Function name style
- π Pythonic Constant name style
- π Significance of CapWords or CamelCase in Python

## Requirements
### General
- π© Allowed editors: `vi`, `vim`, `emacs`
- π© All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- π© All your files should end with a new line
- π© The first line of all your files should be exactly `#!/usr/bin/python3`
- π© __Libraries imported in your Python files must be organized in alphabetical order__
- π© A `README.md` file, at the root of the folder of the project, is mandatory
- π© Your code should use the `PEP 8` style
- π© All your files must be executable
- π© The length of your files will be tested using `wc`
- π© All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- π© You must use [get](https://docs.python.org/3.4/library/stdtypes.html#dict.get) to access to dictionary value by key (it wonβt throw an exception if the key doesnβt exist in the dictionary)
- π© Your code should not be executed when imported (by using `if __name__ == "__main__":`)

By Estefania Ruiz π¦ From Holberton School πͺ
