# Looping throught list - orders name
orders = ["shivam", "aman", "carlos"]

for name in orders:
    print(f"Oder ready for {name}")


# Task Completion Tracker
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
    updated_task = []
    for task in tasks:
        updated_task.append(f"Completed: {task}")
    return updated_task