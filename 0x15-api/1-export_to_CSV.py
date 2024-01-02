#!/usr/bin/python3
""" Export data to csv
"""
from requests import get
import csv
from sys import argv


if __name__ == '__main__':
    module = "0-gather_data_from_an_API"
    data = __import__(module)
    employee_id = argv[1]
    employee_name, todos = data.get_data_from_api(employee_id)

    if employee_name and todos:
        file_name = "{}.csv".format(employee_id)

        with open(file_name, "w", newline="") as to_file:
            csv_writer = csv.writer(to_file)

            for task in todos:
                csv_writer.writerow([
                    employee_id, employee_name,
                    "True" if task["completed"] else "False",
                    task["title"]
                    ])
