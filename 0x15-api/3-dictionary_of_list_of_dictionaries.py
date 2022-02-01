#!/usr/bin/python3
'''
Python script to export data in the JSON format.
'''
import json
import requests


if __name__ == "__main__":

    url_users = 'https://jsonplaceholder.typicode.com/users/'
    employee = requests.get(url_users).json()
    all_employees = requests.get('https://jsonplaceholder.typicode.com/todos/')
    all_user = {}

    for i in employee:
        all_task = []
        for j in all_employees.json():
            if j.get('userId') == i.get('id'):
                dict_task = {"username": i.get('username'),
                             "task": j.get('title'),
                             "completed": j.get('completed')}
                all_task.append(dict_task)
        all_user[i.get('id')] = all_task

    with open("todo_all_employees.json", 'w') as f:
        json.dump(all_user, f)
