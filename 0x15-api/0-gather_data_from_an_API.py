#!/usr/bin/python3
"""Returns inforamation to-do list for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed_titles = list(map(lambda t: t.get("title"), filter(lambda t: t.get("completed"), todos)))

employee_name = user.get("name")
total_tasks = len(todos)
completed_tasks = len(completed_titles)
print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

for title in completed_titles:
    print(f"\t {title}")
