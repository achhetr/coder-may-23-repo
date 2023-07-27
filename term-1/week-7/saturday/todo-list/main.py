from clear import clear_terminal

# a way to store all the information
tasks = {} # name is the key and mark is the value


# Home work: add notes to task, add task id to search from name or id
# data is not persisted

# functions
def print_options():
    clear_terminal()

    print("""
    Todo List options

    Enter options from the list below

    [1] List all tasks
    [2] Add new task
    [3] Remove task
    [4] Mark task as completed
    [Enter anything else to exit..]
    """)

def list_tasks():
    clear_terminal()
    print("----------Your Tasks-----------")

    if len(tasks.keys()) < 1:
        print("----------XXXXXX-----------")
        print("------Empty task list------")
        print("----------XXXXXX-----------")


    for name, _ in tasks.items():
        print(get_task(name))

def remove_task():
    list_tasks()

    print("----------Remove Task-----------")
    task = input("Enter your task name> ")

    try:
        del tasks[task]
        print(task, "was deleted")
    except KeyError:
        print(task, "was not found")


def add_task():
    clear_terminal()
    print("----------Add new Task-----------")
    task = input("Enter your task name> ")
    tasks[task] = False
    clear_terminal()
    print("New task added")
    print(get_task(task))

def mark_task():
    list_tasks()

    print("----------Mark your task-----------")
    task = input("Enter your task name> ")

    try:
        tasks[task]
    except KeyError:
        print(task, "does exists")
    else:
        tasks[task] = True
        list_tasks()
    

def get_task(name):
    if tasks[name]:
        return f"'{name}' - (√)"

    return f"'{name}' - (X)"


# functions ended

# run our application
# present user with an option
# to get input from the user
# perform operation if needed
while True:
    print_options()

    option = int(input("Enter your selection> "))

    match option:
        case 1:
            list_tasks()
        case 2:
            add_task()
        case 3:
            remove_task()
        case 4:
            mark_task()
        case _:
            break

    input("press enter to continue....")

print("Application closed")

# error handling
