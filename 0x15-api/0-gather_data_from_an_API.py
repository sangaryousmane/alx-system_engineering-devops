#!/usr/bin/python3
# Get employees data from an API
from sys import argv
from requests import get
from requests.exceptions import RequestException


def get_data_from_api(employee_id):
    """ Get employees data from an API
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"

    try:
        employee_url = f"{base_url}/{employee_id}"
        todos_url = f"{base_url}/{employee_id}/todos"
        employee_data = get(employee_url).json()
        todos_data = get(todos_url).json()

        return employee_data["name"], todos_data

    except RequestException as e:
        print("Sorry, wrong ID: ", employee_id)
        return None, None


if __name__ == '__main__':
    employee_id = argv[1]
    name, todos = get_data_from_api(employee_id)
    completed_task = len([todo for todo in todos if todo.get("completed")])
    todo_len = len(todos)
    print(f"Employee {name} is done with tasks({completed_task}/{todo_len})")

    for todo in todos:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
