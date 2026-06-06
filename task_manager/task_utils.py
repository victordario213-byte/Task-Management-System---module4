from datetime import datetime

from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return False
    if not isinstance(index, int) or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return False

    tasks[index - 1]["completed"] = True
    return True
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks.")
        return pending_tasks

    print("\nPending Tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']} - due {task['due_date']}")
        print(f"   Description: {task['description']}")
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0

    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress