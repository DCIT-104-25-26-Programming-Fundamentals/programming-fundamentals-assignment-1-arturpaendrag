# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# FUNCTION 1 — Addition
# =============================================================================
 
def add(num1, num2):
    """
    Add two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: The sum of num1 and num2
    """
    return num1 + num2
 
 
# =============================================================================
# FUNCTION 2 — Subtraction
# =============================================================================
 
def subtract(num1, num2):
    """
    Subtract two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: The difference (num1 - num2)
    """
    return num1 - num2
 
 
# =============================================================================
# FUNCTION 3 — Multiplication
# =============================================================================
 
def multiply(num1, num2):
    """
    Multiply two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: The product of num1 and num2
    """
    return num1 * num2
 
 
# =============================================================================
# FUNCTION 4 — Division
# =============================================================================
 
def divide(num1, num2):
    """
    Divide two numbers.
    Handles division by zero.
    
    Args:
        num1 (float): First number (dividend)
        num2 (float): Second number (divisor)
        
    Returns:
        float: The quotient (num1 / num2), or None if division by zero
    """
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return num1 / num2
 
 
# =============================================================================
# FUNCTION 5 — Modulus (Remainder)
# =============================================================================
 
def modulus(num1, num2):
    """
    Find the remainder of division.
    
    Args:
        num1 (float): First number (dividend)
        num2 (float): Second number (divisor)
        
    Returns:
        float: The remainder (num1 % num2), or None if division by zero
    """
    if num2 == 0:
        print("Error: Cannot find modulus with zero.")
        return None
    return num1 % num2
 
 
# =============================================================================
# FUNCTION 6 — Exponentiation
# =============================================================================
 
def exponentiate(num1, num2):
    """
    Raise a number to a power.
    
    Args:
        num1 (float): Base number
        num2 (float): Exponent
        
    Returns:
        float: num1 raised to the power of num2
    """
    return num1 ** num2
 
 
# =============================================================================
# FUNCTION 7 — Display Menu
# =============================================================================
 
def display_menu():
    """
    Display the calculator menu options.
    """
    print("\n" + "=" * 30)
    print("     SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
    print("=" * 30)
 
 
# =============================================================================
# FUNCTION 8 — Get Numbers from User
# =============================================================================
 
def get_numbers():
    """
    Prompt the user to enter two numbers.
    Validates that the input is numeric.
    
    Returns:
        tuple: (num1, num2) if valid, or (None, None) if invalid
    """
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.\n")
        return None, None
 
 
# =============================================================================
# MAIN BLOCK
# =============================================================================
 
def main():
    """
    Main program loop for the calculator.
    """
    print("\n" + "=" * 30)
    print("   WELCOME TO THE CALCULATOR")
    print("=" * 30)
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "1":
            # Addition
            num1, num2 = get_numbers()
            if num1 is not None:
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}\n")
        
        elif choice == "2":
            # Subtraction
            num1, num2 = get_numbers()
            if num1 is not None:
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}\n")
        
        elif choice == "3":
            # Multiplication
            num1, num2 = get_numbers()
            if num1 is not None:
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}\n")
        
        elif choice == "4":
            # Division
            num1, num2 = get_numbers()
            if num1 is not None:
                result = divide(num1, num2)
                if result is not None:
                    # Round to 2 decimal places
                    print(f"Result: {num1} / {num2} = {result:.2f}\n")
                else:
                    print()
        
        elif choice == "5":
            # Modulus
            num1, num2 = get_numbers()
            if num1 is not None:
                result = modulus(num1, num2)
                if result is not None:
                    print(f"Result: {num1} % {num2} = {result}\n")
                else:
                    print()
        
        elif choice == "6":
            # Exponentiation
            num1, num2 = get_numbers()
            if num1 is not None:
                result = exponentiate(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}\n")
        
        elif choice == "7":
            # Quit
            print("\nGoodbye!\n")
            break
        
        else:
            # Invalid choice
            print("Error: Please select a valid operation (1-7).\n")
 
 
if __name__ == "__main__":
    main()