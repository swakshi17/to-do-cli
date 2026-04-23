tasks = []

while True:
    task = input("Enter task (or 'q'): ")
    if task == 'q':
        break
    tasks.append(task)

print("Tasks:", tasks)
