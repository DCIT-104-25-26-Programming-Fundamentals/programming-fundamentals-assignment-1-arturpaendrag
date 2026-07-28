# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PART A — Print the First N Terms
# =============================================================================

def generate_fibonacci_terms(n):
    """
    Generate and print the first N Fibonacci numbers.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: A list containing the first N Fibonacci numbers
    """
    # Validate input
    if n <= 0:
        return None
    
    # Initialize the sequence with the first two terms
    fib_sequence = []
    
    if n >= 1:
        fib_sequence.append(0)
    if n >= 2:
        fib_sequence.append(1)
    
    # Generate the rest using a loop
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    
    return fib_sequence


# =============================================================================
# PART B — Check if a Number is Fibonacci
# =============================================================================

def is_fibonacci_number(num):
    """
    Check if a given number is in the Fibonacci sequence.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if num is a Fibonacci number, False otherwise
    """
    # Handle negative numbers (not in standard Fibonacci sequence)
    if num < 0:
        return False
    
    # Generate Fibonacci numbers until we find num or exceed it
    a, b = 0, 1
    
    # Check if num is the first Fibonacci number (0)
    if num == a:
        return True
    
    # Loop through the sequence
    while b <= num:
        if b == num:
            return True
        # Generate next Fibonacci number
        a, b = b, a + b
    
    return False


# =============================================================================
# HELPER FUNCTION — Display Fibonacci Sequence
# =============================================================================

def display_fibonacci_sequence(sequence):
    """
    Display the Fibonacci sequence in a formatted way.
    
    Args:
        sequence (list): List of Fibonacci numbers to display
    """
    sequence_str = " ".join(str(num) for num in sequence)
    print(f"Fibonacci sequence: {sequence_str}")


# =============================================================================
# MAIN BLOCK — Menu System
# =============================================================================

def main():
    """Main program with menu to choose between Part A and Part B."""
    
    while True:
        print("\n" + "=" * 60)
        print("FIBONACCI SEQUENCE GENERATOR")
        print("=" * 60)
        print("A. Print the first N terms of the Fibonacci sequence")
        print("B. Check if a number is a Fibonacci number")
        print("C. Exit")
        print("=" * 60)
        
        choice = input("Select an option (A, B, or C): ").strip().upper()
        
        if choice == "A":
            # Part A: Print first N terms
            try:
                n = int(input("\nHow many terms? "))
                
                # Validate input
                if n <= 0:
                    print("Error: Number of terms must be a positive integer.")
                    continue
                
                # Generate the sequence
                fib_sequence = generate_fibonacci_terms(n)
                
                # Display the sequence
                display_fibonacci_sequence(fib_sequence)
                
            except ValueError:
                print("Error: Please enter a valid positive integer.")
        
        elif choice == "B":
            # Part B: Check if number is Fibonacci
            try:
                num = int(input("\nEnter a number to check: "))
                
                # Check if number is Fibonacci
                if is_fibonacci_number(num):
                    print(f"{num} is a Fibonacci number.")
                else:
                    print(f"{num} is NOT a Fibonacci number.")
                
            except ValueError:
                print("Error: Please enter a valid integer.")
        
        elif choice == "C":
            print("\nThank you for using the Fibonacci Sequence Generator!")
            break
        
        else:
            print("Error: Please select a valid option (A, B, or C).")


if __name__ == "__main__":
    main()