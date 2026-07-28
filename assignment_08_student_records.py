# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# FUNCTION 1 — Add a Student
# =============================================================================
 
def add_student(students):
    """
    Add a new student record to the list.
    Collects name, ID, and multiple scores.
    
    Args:
        students (list): The list of student dictionaries
    """
    print()
    
    try:
        # Get student name
        name = input("Student name: ").strip()
        if not name:
            print("Error: Student name cannot be empty.\n")
            return
        
        # Get student ID
        student_id = int(input("Student ID: "))
        
        # Check if ID already exists
        for student in students:
            if student["id"] == student_id:
                print(f"Error: Student ID {student_id} already exists.\n")
                return
        
        # Get number of scores
        num_scores = int(input("How many scores? "))
        
        if num_scores <= 0:
            print("Error: Number of scores must be positive.\n")
            return
        
        # Collect scores
        scores = []
        for i in range(num_scores):
            score = float(input(f"Enter score {i + 1}: "))
            
            # Validate score range (optional: 0-100)
            if score < 0 or score > 100:
                print("Warning: Score is outside typical range (0-100).")
            
            scores.append(score)
        
        # Create student dictionary
        student = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        
        # Add to list
        students.append(student)
        print(f"Student \"{name}\" added successfully.\n")
    
    except ValueError:
        print("Error: Please enter valid data (numbers for ID and scores).\n")
 
 
# =============================================================================
# FUNCTION 2 — Display All Students
# =============================================================================
 
def display_all_students(students):
    """
    Display all students in a formatted table.
    Shows name, ID, scores, and average.
    
    Args:
        students (list): The list of student dictionaries
    """
    print()
    
    # Check if the list is empty
    if len(students) == 0:
        print("No students have been added yet.\n")
        return
    
    # Print table header
    print("-" * 70)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<20} {'Average':<10}")
    print("-" * 70)
    
    # Print each student
    for student in students:
        name = student["name"]
        student_id = student["id"]
        scores = student["scores"]
        
        # Calculate average
        average = sum(scores) / len(scores)
        
        # Format scores as comma-separated string
        scores_str = ", ".join(str(score) for score in scores)
        
        # Print row
        print(f"{name:<20} {student_id:<12} {scores_str:<20} {average:>7.2f}")
    
    print("-" * 70)
    print()
 
 
# =============================================================================
# FUNCTION 3 — Calculate Average Score for a Specific Student
# =============================================================================
 
def calculate_average(students):
    """
    Find a student by ID and calculate their average score.
    
    Args:
        students (list): The list of student dictionaries
    """
    print()
    
    # Check if the list is empty
    if len(students) == 0:
        print("No students in the system.\n")
        return
    
    try:
        # Get student ID from user
        student_id = int(input("Enter student ID: "))
        
        # Search for the student
        found = False
        for student in students:
            if student["id"] == student_id:
                found = True
                name = student["name"]
                scores = student["scores"]
                
                # Calculate average
                average = sum(scores) / len(scores)
                
                # Display result
                print(f"{name}'s average score: {average:.2f}\n")
                break
        
        # If student not found
        if not found:
            print(f"Error: Student ID {student_id} not found.\n")
    
    except ValueError:
        print("Error: Please enter a valid student ID (number).\n")
 
 
# =============================================================================
# FUNCTION 4 — Display Menu
# =============================================================================
 
def display_menu():
    """
    Display the main menu options.
    """
    print("=" * 50)
    print("   STUDENT RECORD SYSTEM MENU")
    print("=" * 50)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    print("=" * 50)
 
 
# =============================================================================
# MAIN BLOCK
# =============================================================================
 
def main():
    """
    Main program loop for the student record system.
    """
    # Initialize the students list
    students = []
    
    print("\n" + "=" * 50)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 50 + "\n")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Add a student
            add_student(students)
        
        elif choice == "2":
            # Display all students
            display_all_students(students)
        
        elif choice == "3":
            # Calculate average for a specific student
            calculate_average(students)
        
        elif choice == "4":
            # Quit
            print("\nThank you for using the Student Record System. Goodbye!\n")
            break
        
        else:
            # Invalid choice
            print("Error: Please enter a valid choice (1-4).\n")
 
 
if __name__ == "__main__":
    main()