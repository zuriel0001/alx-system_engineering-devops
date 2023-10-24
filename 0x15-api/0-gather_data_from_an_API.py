#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID
   The script uses particular REST API.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    for task in todos:
        if task.get("completed"):
            completed.append(task.get("title"))

    #  completed = [task.get("title") for task in todos
        # if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
