#!/usr/bin/python3
'''
Python script to export data in the CSV format.
'''
import csv
import requests
from sys import argv


if __name__ == "__main__":

    id_employ = argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(id_employ)).json()

    EMPLOYEE_NAME = employee.get('username')

    all_employees = requests.get('https://jsonplaceholder.typicode.com/todos/')

    filename = id_employ + '.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')

    for i in all_employees.json():
        if i.get('userId') == int(id_employ):
            writer.writerow([id_employ, EMPLOYEE_NAME,
                            i.get('completed'), i.get('title')])
