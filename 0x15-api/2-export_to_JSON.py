#!/usr/bin/python3
'''
Python script to export data in the JSON format.
'''
import json
import requests
from sys import argv


if __name__ == "__main__":

    id_employ = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(id_employ)).json()

    EMPLOYEE_NAME = employee.get('username')

    all_employees = requests.get('https://jsonplaceholder.typicode.com/todos/')

    owner_task = []
    dict_employ = {}

    for i in all_employees.json():
        # if i.get('userId') == int(id_employ):
            dict_task = {"task": i['title'],
                         "completed": i['completed'],
                         "username": EMPLOYEE_NAME}
            owner_task.append(dict_task)
    dict_employ[id_employ] = owner_task

    filename = id_employ + '.json'
    with open(filename, 'w') as f:
        json.dump(dict_employ, f)
