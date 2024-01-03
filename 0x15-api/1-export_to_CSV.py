#!/usr/bin/python3
""" Export data to csv
"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    module = "0-gather_data_from_an_API"
    data = __import__(module)
    employee_id = argv[1]
    _, todos = data.get_data_from_api(employee_id)
    username = get(f'{base_url}/{employee_id}').json()
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "w", newline="") as to_file:
        csv_writer = csv.writer(to_file)

        for task in todos:
            csv_writer.writerow([
                employee_id, username,
                "True" if task["completed"] else "False",
                task["title"]
                ])
