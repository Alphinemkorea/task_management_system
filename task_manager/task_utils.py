from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    if (
        validate_task_title(title)
        and validate_task_description(description)
        and validate_due_date(due_date)
    ):

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully.")

    else:
        print("Task not added.")


def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            print("Task marked as complete.")
            return

    print("Task not found.")


def view_pending_tasks(tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for task in pending_tasks:
            print(
                f"Title: {task['title']}\n"
                f"Description: {task['description']}\n"
                f"Due Date: {task['due_date']}\n"
            )


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100
    return progress