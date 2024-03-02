# todolist.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed.')
    else:
        print(f'Task "{task}" not found.')

def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

# Example usage
add_task("Complete homework")
list_tasks()
remove_task("Complete homework")
list_tasks()

