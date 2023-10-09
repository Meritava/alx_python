import requests
import json

def export_all_employee_tasks():
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve all users
    users_url = f"{base_url}/users"
    response = requests.get(users_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        users_data = response.json()
        
        # Create a dictionary to store tasks for all employees
        all_tasks = {}

        # Iterate over each user to fetch their tasks
        for user in users_data:
            user_id = user['id']
            username = user['username']

            # Make a GET request to retrieve the user's TODO list
            todos_url = f"{base_url}/users/{user_id}/todos"
            todos_response = requests.get(todos_url)

            # Check if the request was successful (status code 200)
            if todos_response.status_code == 200:
                todos_data = todos_response.json()

                # Create a list of dictionaries for each task
                tasks_list = [
                    {
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": username
                    }
                    for task in todos_data
                ]

                # Add the tasks to the dictionary using the user ID as the key
                all_tasks[user_id] = tasks_list
        
        # Export data to a JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_tasks, json_file, indent=4)
        
        print(f"Data exported to {json_filename}")

    else:
        print("Failed to fetch data from the API.")

if __name__ == "__main__":
    export_all_employee_tasks()
