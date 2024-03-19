#!/usr/bin/python3
"""
Given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

HTTP_OK = 200

def get_employee_todo_progress(employee_id):
    # Hypothetical API endpoint
    url = f"https://jsonplaceholder.typicode.com/todos"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == HTTP_OK:
        data = response.json()

        # Extract necessary information from the response
        employee_name = data['employee_name']
        tasks = data['tasks']
        done_tasks = [task for task in tasks if task['completed']]

        # Calculate progress
        total_tasks = len(tasks)
        number_of_done_tasks = len(done_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    else:
        print(f"Failed to fetch data for employee ID {employee_id}. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
