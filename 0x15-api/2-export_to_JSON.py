#!/usr/bin/python3
""" Export to json
"""

import json
from requests import get
from sys import argv


if __name__ == '__main__':
    module = "0-gather_data_from_an_API"
    data = __import__(module)
    employee_id = argv[1]
    employee_name, todos = data.get_data_from_api(employee_id)

    if employee_name and todos:
        JSON_DATA = {
                employee_id: [{
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                    } for task in todos

                    ]}
    file_name = f"{employee_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(JSON_DATA, json_file, indent=4)
