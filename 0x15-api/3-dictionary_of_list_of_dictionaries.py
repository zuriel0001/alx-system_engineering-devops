#!/usr/bin/python3
"""Script to export to-do list for all employees to JSON format
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": tsk.get("title"),
                "completed": tsk.get("completed"),
                "username": u.get("username")
            } for tsk in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
