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
        print("Task added successfully!")

    else:
        print("Task not added.")


def mark_task_as_complete(tasks, task_number):

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!")

    else:
        print("Invalid task number.")


def view_pending_tasks(tasks):

    pending_tasks = []

    for task in tasks:
        if task["completed"] is False:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks.")

    else:
        print("\nPending Tasks:")

        for index, task in enumerate(pending_tasks, start=1):
            print(f"{index}. {task['title']}")
            print(task["description"])
            print(task["due_date"])


def calculate_progress(tasks):

    if len(tasks) == 0:
        return 0

    completed_count = 0

    for task in tasks:
        if task["completed"]:
            completed_count += 1

    progress = (completed_count / len(tasks)) * 100

    return progress