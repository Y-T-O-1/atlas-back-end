#!/usr/bin/python3
"""
Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    EMPLOYEE_ID = sys.argv[1]

    # Fetch user data to get the employee name
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    )
    user_data = user_response.json()
    if user_response.status_code != 200:
        print("RequestError:", user_response.status_code)
        sys.exit(1)

    employee_name = user_data["name"]

    # Fetch TODO list for the employee
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos"
    )
    todos_data = todos_response.json()
    if todos_response.status_code != 200:
        print("RequestError:", todos_response.status_code)
        sys.exit(1)

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")
