# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# FUNCTION 1 — Add a Task
# =============================================================================
 
def add_task(tasks):
    """
    Prompt the user to enter a task and add it to the list.
    
    Args:
        tasks (list): The list of tasks
    """
    task_description = input("Enter task: ").strip()
    
    # Only add if the user entered something
    if task_description:
        tasks.append(task_description)
        print(f"Task added: \"{task_description}\"\n")
    else:
        print("Error: Task cannot be empty. Please try again.\n")
 
 
# =============================================================================
# FUNCTION 2 — View All Tasks
# =============================================================================
 
def view_tasks(tasks):
    """
    Display all tasks in the list with their numbers.
    If the list is empty, display a friendly message.
    
    Args:
        tasks (list): The list of tasks
    """
    # Check if the list is empty
    if len(tasks) == 0:
        print("Your to-do list is empty. Add a task to get started!\n")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print()
 
 
# =============================================================================
# FUNCTION 3 — Delete a Task
# =============================================================================
 
def delete_task(tasks):
    """
    Display all tasks, ask the user which task to delete, and remove it.
    Handles invalid task numbers gracefully.
    
    Args:
        tasks (list): The list of tasks
    """
    # First, check if there are any tasks to delete
    if len(tasks) == 0:
        print("Your to-do list is empty. Nothing to delete.\n")
        return
    
    # Show all tasks
    print("Your Tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")
    print()
    
    # Ask which task to delete
    try:
        task_number = int(input("Enter task number to delete: "))
        
        # Validate the task number
        if task_number < 1 or task_number > len(tasks):
            print(f"Error: Please enter a number between 1 and {len(tasks)}.\n")
        else:
            # Remove the task (convert to 0-based index)
            removed_task = tasks.pop(task_number - 1)
            print(f"Task \"{removed_task}\" has been removed.\n")
    
    except ValueError:
        print("Error: Please enter a valid number.\n")
 
 
# =============================================================================
# FUNCTION 4 — Display Menu
# =============================================================================
 
def display_menu():
    """
    Display the main menu options.
    """
    print("=" * 30)
    print("     TO-DO LIST MENU")
    print("=" * 30)
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("=" * 30)
 
 
# =============================================================================
# MAIN BLOCK
# =============================================================================
 
def main():
    """
    Main program loop that runs the to-do list application.
    """
    # Initialize the tasks list
    tasks = []
    
    print("\n" + "=" * 30)
    print("   WELCOME TO YOUR TO-DO LIST")
    print("=" * 30 + "\n")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Add a task
            add_task(tasks)
        
        elif choice == "2":
            # View all tasks
            print()
            view_tasks(tasks)
        
        elif choice == "3":
            # Delete a task
            print()
            delete_task(tasks)
        
        elif choice == "4":
            # Quit
            print("\nGoodbye!\n")
            break
        
        else:
            # Invalid choice
            print("Error: Please enter a valid choice (1-4).\n")
 
 
if __name__ == "__main__":
    main()