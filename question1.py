# Define a function to reverse a string
def reverse_string(s):
    return s[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
reversed_output = reverse_string(user_input)
print("Reversed string:", reversed_output)
