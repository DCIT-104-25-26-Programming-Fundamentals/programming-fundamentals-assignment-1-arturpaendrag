# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """
    Calculate the sum of all numbers in a list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int/float: The sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """
    Calculate the average of all numbers in a list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        float: The average of all numbers
    """
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """
    Find the maximum value in a list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int/float: The largest number in the list
    """
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_minimum(numbers):
    """
    Find the minimum value in a list.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        int/float: The smallest number in the list
    """
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value



# MAIN BLOCK



if __name__ == "__main__":
    try:
        # Get the count of numbers
        n = int(input("How many numbers? "))
        
        # Validate that N is positive
        if n <= 0:
            print("Error: Number of elements must be a positive integer.")
        else:
            # Initialize list to store numbers
            numbers = []
            
            # Read N numbers from user
            for i in range(n):
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
            
            # Calculate statistics using functions
            total = calculate_sum(numbers)
            average = calculate_average(numbers)
            maximum = find_maximum(numbers)
            minimum = find_minimum(numbers)
            
            # Display results
            print("\nResults:")
            print(f"Sum:     {total}")
            print(f"Average: {average}")
            print(f"Maximum: {maximum}")
            print(f"Minimum: {minimum}")
            
    except ValueError:
        print("Error: Please enter valid numbers.")