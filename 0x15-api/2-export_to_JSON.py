#!/usr/bin/python3
"""Extend the last Python script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{user_id}")
    todos_response = requests.get(f"{base_url}todos",
                                  params={"userId": user_id})

    user = user_response.json()
    todos = todos_response.json()
    username = user.get("username")

    tasks = [
        {"task": todo["title"],
         "completed": todo["completed"],
         "username": username}
        for todo in todos
    ]
    user_data = {user_id: tasks}

    with open(f"{user_id}.json", "w") as file:
        json.dump(user_data, file)

