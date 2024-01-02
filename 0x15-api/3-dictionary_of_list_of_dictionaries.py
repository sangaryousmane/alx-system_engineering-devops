#!/usr/bin/python3
""" Records all tasks from all employees
"""
import json
from requests import get
from requests.exceptions import RequestException


if __name__ == '__main__':
    module = "0-gather_data_from_an_API"
    data = __import__(module)

    try:
        base_url = "https://jsonplaceholder.typicode.com/"
        users_url = f"{base_url}users"

        all_employees_data = {}
        employee_ids = [user["id"] for user in get(users_url).json()]
        users = [user["username"] for user in get(users_url).json()]

        for employee_id, username in zip(employee_ids, users):
            employee_name, todos = data.get_data_from_api(employee_id)

            task_data = [
                    {
                        "username": username,
                        "task": task['title'],
                        "completed": task["completed"]
                    } for task in todos
                    ]
            all_employees_data[employee_id] = task_data
           
            filename = "todo_all_employees.json"
            with open (filename, "w") as json_file:
                json.dump(all_employees_data, json_file, indent=4)
    except RequestException as e:
        print(e.response)
