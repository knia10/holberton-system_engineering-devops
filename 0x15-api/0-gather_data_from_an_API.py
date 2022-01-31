#!/usr/bin/python3
'''
script that, using this REST API, for a given employee ID,
returns information about his/her TODo list progress.
'''
import requests
from sys import argv

if __name__ == "__main__":
    ''' returns information about his/her TODo list progress.'''

    id_employ = argv[1]
    employee = requests.get(f"https://jsonplaceholder.typicode.com/users\
                {id_employ}")

    EMPLOYEE_NAME = employee.json().get('name')

    all_employees = requests.get('https://jsonplaceholder.typicode.com/todos/')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for i in all_employees.json():
        if i.get('userId') == int(id_employ):
            TOTAL_NUMBER_OF_TASKS += 1
            if i.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(i.get('title'))
    print(f"Employee {EMPLOYEE_NAME} is done with\
        ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")

    for j in TASK_TITLE:
        print(f"\t {j}")
