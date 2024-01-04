#!/usr/bin/python3
"""Returns info uber to-do list, for a given employee ID"""

import requests
import sys

def main():
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{employee_id}")
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
    user = user_response.json()
    todos = todos_response.json()
    completed_tasks = [todo['title'] for todo in todos if todo.get('completed')]

    user_name = user.get('name', 'Unknown User')
    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task_title in completed_tasks:
        print(f"\t {task_title}")
if __name__ == "__main__":
    main()
