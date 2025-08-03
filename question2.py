def most_frequent_numbers(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # find the highest frequency value
    max_count = max(frequency.values())

    # collect all numbers with the highest frequency
    most_frequent = [num for num, count in frequency.items() if count == max_count]

    return most_frequent

# get input from user
user_input = input("Enter a list of integers separated by commas (e.g. 4,3,3,3,2,2,1): ")

# convert input to a list of integers
input_list = [int(x.strip()) for x in user_input.split(",")]

# find and print the most frequent numbers
result = most_frequent_numbers(input_list)
print(result)
