#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{base_url}users").json()

    all_users_todo_data = {}
    for user in users:
        user_id = user["id"]
        todos = requests.get(f"{base_url}todos",
                             params={"userId": user_id}).json()

        all_users_todo_data[user_id] = [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            }
            for todo in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_users_todo_data, jsonfile)
