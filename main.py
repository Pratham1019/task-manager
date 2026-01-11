import tasks

def main():
    json_file_path = "tasks.json"
    json_data = tasks.load_tasks(json_file_path)
    
    while (True):
        changed = False
    
        print("\n=== Task Manager Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice: int = get_input()
        
        match choice:
            case 1:
                task = input("Enter task: ")
                tasks.add_task(json_data, task)
                changed = True
                
            case 2:
                tasks.display_tasks(json_data)

            case 3:
                tasks.display_tasks(json_data)
                try:
                    task_no = int(input("Enter task number: "))
                except ValueError:
                    print("Invalid number.")
                    continue
                
                if not tasks.complete_task(json_data, task_no):
                    print("Did not find a task at that position")
                else:
                    changed = True
                
            case 4:
                if len(json_data['tasks']) == 0:
                    print("Nothing to delete")
                else:
                    tasks.display_tasks(json_data)
                    try:
                        task_no = int(input("Enter task number: "))
                    except ValueError:
                        print("Invalid number.")
                        continue
                    
                    if not tasks.delete_task(json_data, task_no):
                        print("Did not find a task at that position")
                    else:
                        changed = True
                
            case 5:
                print("Exiting...")
                break
        
        if changed:
            tasks.save_tasks(json_file_path, json_data)            
                
def get_input() -> int:
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4, 5]:
            raise ValueError
            
    except (TypeError, ValueError):
        print("Invalid choice.")
        return get_input()

    return choice

if __name__ == "__main__":
    main()