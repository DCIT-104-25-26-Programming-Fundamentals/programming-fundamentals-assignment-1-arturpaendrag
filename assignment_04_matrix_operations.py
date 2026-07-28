# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_matrix(matrix, label="Matrix"):
    """
    Display a matrix in a neat, aligned grid format.
    
    Args:
        matrix (list of lists): The matrix to display
        label (str): Label for the matrix
    """
    print(f"\n{label}:")
    for row in matrix:
        # Format each value to align in columns
        formatted_row = " ".join(f"{value:6.1f}" for value in row)
        print(formatted_row)


def read_matrix(rows, cols, prompt=""):
    """
    Read a matrix from user input.
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        prompt (str): Optional label for the matrix
        
    Returns:
        list of lists: The matrix entered by the user
    """
    matrix = []
    if prompt:
        print(f"\n{prompt}")
    
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                values = [float(x) for x in row_input.split()]
                
                if len(values) != cols:
                    print(f"Error: Expected {cols} values, got {len(values)}. Try again.")
                    continue
                
                matrix.append(values)
                break
            except ValueError:
                print("Error: Please enter numbers separated by spaces.")
    
    return matrix



# PART A — Transpose a Matrix



def transpose_matrix(matrix):
    """
    Compute the transpose of a matrix.
    Rows become columns, columns become rows.
    
    Args:
        matrix (list of lists): The original M x N matrix
        
    Returns:
        list of lists: The transposed N x M matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new matrix with swapped dimensions (N x M)
    transposed = []
    
    # Use nested loops to swap rows and columns
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    return transposed



# PART B — Add Two Matrices



def add_matrices(matrix1, matrix2):
    """
    Add two matrices of the same size.
    Result[i][j] = Matrix1[i][j] + Matrix2[i][j]
    
    Args:
        matrix1 (list of lists): First M x N matrix
        matrix2 (list of lists): Second M x N matrix
        
    Returns:
        list of lists: The sum matrix (M x N)
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Create result matrix filled with zeros
    result = []
    
    # Use nested loops to add corresponding elements
    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(matrix1[row][col] + matrix2[row][col])
        result.append(new_row)
    
    return result



# PART C — Multiply Two Matrices



def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply two matrices: A (M x N) × B (N x P) = Result (M x P)
    Each element in the result is the dot product of the corresponding
    row in A and column in B.
    
    Args:
        matrix_a (list of lists): First matrix (M x N)
        matrix_b (list of lists): Second matrix (N x P)
        
    Returns:
        list of lists: The product matrix (M x P)
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # Verify that multiplication is possible
    if cols_a != rows_b:
        return None
    
    # Create result matrix (M x P)
    result = []
    
    # Use nested loops to compute the product
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            # Compute dot product of row i of A and column j of B
            sum_product = 0
            for k in range(cols_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    
    return result



# MAIN BLOCK - Menu System



def main():
    """Main program with menu to choose which operation to perform."""
    
    while True:
        print("\n" + "=" * 60)
        print("MATRIX OPERATIONS")
        print("=" * 60)
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Exit")
        print("=" * 60)
        
        choice = input("Select an operation (1-4): ").strip()
        
        if choice == "1":
            # Part A: Transpose
            try:
                rows = int(input("\nEnter number of rows: "))
                cols = int(input("Enter number of columns: "))
                
                if rows <= 0 or cols <= 0:
                    print("Error: Rows and columns must be positive integers.")
                    continue
                
                matrix = read_matrix(rows, cols, "Enter the matrix:")
                transposed = transpose_matrix(matrix)
                
                display_matrix(matrix, "Original Matrix")
                display_matrix(transposed, "Transposed Matrix")
                
            except ValueError:
                print("Error: Please enter valid integers.")
        
        elif choice == "2":
            # Part B: Add Matrices
            try:
                rows = int(input("\nEnter number of rows: "))
                cols = int(input("Enter number of columns: "))
                
                if rows <= 0 or cols <= 0:
                    print("Error: Rows and columns must be positive integers.")
                    continue
                
                matrix1 = read_matrix(rows, cols, "Enter first matrix:")
                matrix2 = read_matrix(rows, cols, "Enter second matrix:")
                
                result = add_matrices(matrix1, matrix2)
                
                display_matrix(matrix1, "Matrix 1")
                display_matrix(matrix2, "Matrix 2")
                display_matrix(result, "Sum (Matrix 1 + Matrix 2)")
                
            except ValueError:
                print("Error: Please enter valid integers.")
        
        elif choice == "3":
            # Part C: Multiply Matrices
            try:
                m = int(input("\nEnter rows in Matrix A: "))
                n = int(input("Enter columns in Matrix A (= rows in Matrix B): "))
                p = int(input("Enter columns in Matrix B: "))
                
                if m <= 0 or n <= 0 or p <= 0:
                    print("Error: Dimensions must be positive integers.")
                    continue
                
                matrix_a = read_matrix(m, n, "Enter Matrix A:")
                matrix_b = read_matrix(n, p, "Enter Matrix B:")
                
                result = multiply_matrices(matrix_a, matrix_b)
                
                if result is None:
                    print("Error: Cannot multiply. Incompatible dimensions.")
                else:
                    display_matrix(matrix_a, "Matrix A")
                    display_matrix(matrix_b, "Matrix B")
                    display_matrix(result, f"Product (A × B)")
                
            except ValueError:
                print("Error: Please enter valid integers.")
        
        elif choice == "4":
            print("\nThank you for using the Matrix Operations program!")
            break
        
        else:
            print("Error: Please select a valid option (1-4).")


if __name__ == "__main__":
    main()