#!/usr/bin/python3
""" Export to json
"""

import json
from requests import get
from sys import argv


if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    module = "0-gather_data_from_an_API"
    data = __import__(module)
    employee_id = argv[1]
    _, todos = data.get_data_from_api(employee_id)
    emp_data = get(f"{users_url}/{employee_id}").json()

    JSON_DATA = {
            employee_id: [{
                "task": task["title"],
                "completed": task["completed"],
                "username": emp_data["username"]
                } for task in todos
                ]}
    file_name = f"{employee_id}.json"

    with open(file_name, "w") as json_file:
        json.dump(JSON_DATA, json_file, indent=4)
