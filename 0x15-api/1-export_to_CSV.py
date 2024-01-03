#!/usr/bin/python3
""" Export data to csv
"""
from csv import DictWriter, QUOTE_ALL
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

    todo_list = []
    for todo in todos:
        todo_dict = {}
        todo_dict.update({"user_ID": employee_id,
                          "username": username['username'],
                          "completed": todo["completed"],
                          "task": todo["title"]})
        todo_list.append(todo_dict)

    with open(file_name, "w", newline="") as to_file:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(to_file, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)
