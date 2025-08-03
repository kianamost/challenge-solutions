def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

# function to check if the matrix is square
def is_square(matrix):
    if not isinstance(matrix, list):
        return False
    n = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            return False
    return True

# keep asking for input until a valid square matrix is provided
while True:
    user_input = input("Enter a square matrix (e.g. [[1,2,3],[4,5,6],[7,8,9]]): ")
    try:
        matrix = eval(user_input)  # try to convert string to list
        if is_square(matrix):
            break  # input is valid
        else:
            print("Error: Matrix must be square and properly formatted.")
    except:
        print("Error: Invalid input. Please enter a list of lists like [[1,2],[3,4]].")

# calculate and print the sum of the diagonal
result = diagonal_sum(matrix)
print("Diagonal sum:", result)
