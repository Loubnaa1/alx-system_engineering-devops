#!/usr/bin/python3
"""Returns info uber to-do list, for a given employee ID"""

import requests
import sys


def main():

    em_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{em_id}")
    todor = requests.get(f"{base_url}todos", params={"userId": em_id})
    user = user_response.json()
    todos = todor.json()
    tasks = [todo['title'] for todo in todos if todo.get('completed')]
    use = user.get('name', 'Unknown User')
    print(f"Employee {use} is done with tasks({len(tasks)}/{len(todos)}):")
    for task_title in tasks:
        print(f"\t {task_title}")


if __name__ == "__main__":
    main()
