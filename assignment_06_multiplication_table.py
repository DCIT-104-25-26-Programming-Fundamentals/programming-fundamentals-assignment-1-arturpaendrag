# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PART A — Single Multiplication Table
# =============================================================================

def print_multiplication_table(n):
    """
    Print the multiplication table for a given number (1 to 12).
    
    Args:
        n (int): The number for which to generate the multiplication table
    """
    print(f"\nMultiplication Table for {n}:")
    print("-" * 35)
    
    # Loop from 1 to 12
    for i in range(1, 13):
        product = n * i
        print(f"{n:4d}  x  {i:2d}  =  {product:4d}")
    
    print("-" * 35)


# =============================================================================
# PART B — Multiple Multiplication Tables (Bonus)
# =============================================================================

def print_multiple_tables(n):
    """
    Print multiplication tables for all numbers from 1 to N.
    Each table is separated by a line.
    
    Args:
        n (int): The upper limit for which to generate tables
    """
    # Loop through each number from 1 to N
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        print("-" * 35)
        
        # Loop from 1 to 12 for each table
        for i in range(1, 13):
            product = num * i
            print(f"{num:4d}  x  {i:2d}  =  {product:4d}")
        
        # Print separator line between tables (except after the last one)
        if num < n:
            print("-" * 35)


# =============================================================================
# MAIN BLOCK — Menu System
# =============================================================================

def main():
    """Main program with menu to choose between Part A and Part B."""
    
    while True:
        print("\n" + "=" * 60)
        print("MULTIPLICATION TABLE GENERATOR")
        print("=" * 60)
        print("A. Print a single multiplication table (1 to 12)")
        print("B. Print multiple multiplication tables (1 to N)")
        print("C. Exit")
        print("=" * 60)
        
        choice = input("Select an option (A, B, or C): ").strip().upper()
        
        if choice == "A":
            # Part A: Single table
            try:
                num = int(input("\nEnter a number: "))
                
                # Validate input
                if num <= 0:
                    print("Error: Number must be a positive integer.")
                    continue
                
                # Print the multiplication table
                print_multiplication_table(num)
                
            except ValueError:
                print("Error: Please enter a valid positive integer.")
        
        elif choice == "B":
            # Part B: Multiple tables
            try:
                n = int(input("\nEnter a number (N): "))
                
                # Validate input
                if n <= 0:
                    print("Error: Number must be a positive integer.")
                    continue
                
                # Print multiple multiplication tables
                print_multiple_tables(n)
                
            except ValueError:
                print("Error: Please enter a valid positive integer.")
        
        elif choice == "C":
            print("\nThank you for using the Multiplication Table Generator!")
            break
        
        else:
            print("Error: Please select a valid option (A, B, or C).")


if __name__ == "__main__":
    main()
    