#!/usr/bin/python3
"""
Exports an employee's todo list to JSON format for a given ID.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": tsk.get("title"),
                "completed": tsk.get("completed"),
                "username": username
            } for tsk in todos]}, jsonfile)
