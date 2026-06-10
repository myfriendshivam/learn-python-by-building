# Use Enumerate

menu = ["Green", "Lemon", "Spiced", "Mint"]

for m in menu:
    print(f"Menu item is {m}")

enum_list = list(enumerate(menu, start=1))

for idx, item  in enum_list:
    print(f"{idx}: {item} chai")

# Numbered Task List
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	# Write your code below this line
    numbered_tasks = []
    for index, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks
