from colorama import Fore, Style, init
import time

init(autoreset=True)

# features:
#     Add tasks
#     View tasks
#     Mark tasks as completed
#     Delete tasks

tasks = []

def add_tasks():
    task = input("Enter a task: ")
    tasks.append(task)
    print(Fore.GREEN + f"Task '{task}' added successfully." + Style.RESET_ALL)

def view_tasks():
    if not tasks:
        print(Fore.YELLOW + "+" + "-" * 22 + "+")
        print("|" + " No tasks to display.".center(22) + "|")
        print("+" + "-" * 22 + "+")
    else:
        print(Fore.BLUE + "+" + "-" * 22 + "+")
        print(Fore.YELLOW + "|" + " Current tasks:".center(22) + "|")
        print(Fore.BLUE + "+" + "-" * 22 + "+")
        for i, task in enumerate(tasks, 1):
            print(f"{Fore.BLUE}| {Fore.YELLOW}{i}. {task}{Fore.BLUE}{Style.RESET_ALL}".ljust(22) + "|")
        print(Fore.BLUE + "+" + "-" * 22 + "+")

def mark_completed():
    while True:
        view_tasks()
        if not tasks:
            print(Fore.RED + "No tasks to mark as complete!" + Style.RESET_ALL)
            return

        try:
            task_number = int(input("Enter the number of the task to mark as completed (0 to exit): "))
            if task_number == 0:
                return  # Exit the mark_completed function
            elif 1 <= task_number <= len(tasks):
                completed_task = tasks[task_number - 1]
                tasks[task_number - 1] = f"{Fore.GREEN}{completed_task} (Completed){Style.RESET_ALL}"
                print(f"Task '{completed_task}' marked as completed.")
            else:
                print(Fore.RED + "Invalid task number." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

def delete_tasks():
    view_tasks()
    if not tasks:
        print(Fore.RED + "There are no tasks to delete. D: " + Style.RESET_ALL)
        return
    
    try:
        task_number = int(input("Enter the number of the task to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number -1)
            print(Fore.GREEN + f"Task '{deleted_task}' deleted successfully. :) " + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

def print_rainbow_text(message):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    for char, color in zip(message, colors * (len(message) // len(colors) + 1)):
        print(color + char, end="", flush=True)  # No type delay

    print(Style.RESET_ALL)

def print_rainbow(message):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    
    for char, color in zip(message, colors * (len(message) // len(colors) + 1)):
        print(color + char, end="", flush=True)
        time.sleep(0.1)
        
    print(Style.RESET_ALL)


while True:
    print("\nTodo List Application")
    print(Fore.YELLOW + "1: Add tasks" + Style.RESET_ALL)
    print(Fore.CYAN + "2: View tasks" + Style.RESET_ALL)
    print(Fore.GREEN + "3: Mark task as Completed" + Style.RESET_ALL)
    print(Fore.RED + "4: Delete tasks" + Style.RESET_ALL)
    print_rainbow_text("5: Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_tasks()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_tasks()
    elif choice == '5':
        print_rainbow("Exiting the program, Peace! :D ")
        break
    else:
        print(Fore.RED + "Invalid choice. Pleas enter a number between 1 and 5." + Style.RESET_ALL)