from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        print("Error: Task title cannot be empty.")
        return False
    return True
    
def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        print("Error: Task description cannot be empty.")
        return False
    return True
    
def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        print("Error: Due date cannot be empty.")
        return False

    try:
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    except ValueError:
        print("Error: Please use the due date format YYYY-MM-DD.")
        return False

    if parsed_date < datetime.now().date():
        print("Error: Due date cannot be in the past.")
        return False

    return True
