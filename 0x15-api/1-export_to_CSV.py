#!/usr/bin/python3
"""Returns information uber TO-DO list and exports the data in for a given employee ID."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{user_id}")
    todos_response = requests.get(f"{base_url}todos", params={"userId": user_id})

    user = user_response.json()
    todos = todos_response.json()
    username = user.get("username")

    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])
