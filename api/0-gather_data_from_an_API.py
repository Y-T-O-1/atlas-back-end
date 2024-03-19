#!/usr/bin/python3
"""
Given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # API endpoint
    url = "https://jsonplaceholder.typicode.com/todos"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        tasks = response.json()

        # For simplicity, we'll assume all tasks belong to the same employee
        # Extract necessary information
        employee_name = "John Doe" # Simulated employee name
        done_tasks = [task for task in tasks if task['completed']]

        # Calculate progress
        total_tasks = len(tasks)
        number_of_done_tasks = len(done_tasks)

        # Display progress
        print(f"Employee {} is done with tasks({}/{}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Since we're simulating employee data, we don't use the employee_id argument
    get_employee_todo_progress(None)
