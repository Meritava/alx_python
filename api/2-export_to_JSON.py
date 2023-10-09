import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve the employee's TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos_data = response.json()
        
        # Calculate the number of completed tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todos_data)

        # Fetch the employee's name from user details
        user_url = f"{base_url}/users/{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name', 'Unknown Employee')

        # Create a list of dictionaries for each task
        tasks_list = [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            for task in todos_data
        ]

        # Create a dictionary to represent the JSON data
        json_data = {
            "USER_ID": tasks_list
        }

        # Export data to a JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        
        print(f"Data exported to {json_filename}")
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task['title']}")

    else:
        print("Failed to fetch data from the API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
