#!/usr/bin/python3

"""
    Returns to-do list information for a given employee ID
   The sceipt uses particular REST API.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for j in data2:
        if j.get('id') == int(argv[1]):
            employee = j.get('name')

    for j in data:
        if j.get('userId') == int(argv[1]):
            total += 1

            if j.get('completed') is True:
                completed += 1
                tasks.append(j.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          completed, total))

    for i in tasks:
        print("\t {}".format(i))
