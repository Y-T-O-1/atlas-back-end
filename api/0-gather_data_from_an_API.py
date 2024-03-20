#!/usr/bin/python3
"""
Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.

    Args:
    employee_id (int): The employee ID.

    Returns:
    dict: The employee's TODO list progress.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        sys.exit(1)


def display_todo_list_progress(employee_id):
    """
    Displays the TODO list progress for a given employee ID.

    Args:
    employee_id (int): The employee ID.
    """
    todo_list = fetch_employee_todo_list(employee_id)
    if todo_list:
        employee_name = todo_list[0]["user"]["name"]
        total_tasks = len(todo_list)
        done_tasks = [task for task in todo_list if task["completed"]]
        total_done_tasks = len(done_tasks)

        print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_list_progress(employee_id)
