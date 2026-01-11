import json

def load_tasks(json_file_path: str) -> dict:
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        return {
            "next_id": 1,
            "tasks": []
        }
        
        
    return json_data

def save_tasks(json_file_path: str, json_data: dict) -> None: 
    try:
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
    except FileNotFoundError:
        print("Could not save it to memory.")
    
def display_tasks(json_data: dict) -> None:
    task_list = json_data['tasks']
    
    if not task_list:
        print("\nNo tasks available.")
        return
    
    print("\nYour Tasks")
    for i, task in enumerate(task_list, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['task']}")


def add_task(json_data: dict, task: str) -> None:
    curr_task = {
        "id": json_data['next_id'],
        "task": task,
        "completed": False
    }
    
    json_data['tasks'].append(curr_task)
    json_data['next_id'] += 1

def delete_task(json_data: dict, pos: int) -> bool:
    tasks = json_data['tasks']
    
    if pos > len(tasks) or pos < 1:
        return False
    
    del tasks[pos - 1]
    return True

def complete_task(json_data: dict, pos: int) -> bool:
    tasks = json_data['tasks']
    
    if pos > len(tasks) or pos < 1:
        return False
    
    if tasks[pos - 1]['completed'] == False:
        tasks[pos - 1]['completed'] = True        
    
    return True
    