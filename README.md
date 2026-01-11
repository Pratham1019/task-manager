# CLI Task Manager (Python)

A simple command-line task manager built using Python.  
Tasks are stored persistently in a JSON file.

## Features
- Add a task
- View all tasks
- Mark a task as completed
- Delete a task
- Persistent storage using a JSON file

## How It Works
- Tasks are loaded from `tasks.json` at program startup
- All operations modify in-memory data
- Changes are written back to the file only when required
- Each task has a unique, non-reusable internal ID

## How to Run
1. Ensure Python 3 is installed
2. Run the program:
   ```bash
   python main.py

## File Structure
- `main.py` – program entry point
- `tasks.py` – task logic
- `tasks.json` – persistent storage

## Notes
- This is a small foundation project focused on clean design