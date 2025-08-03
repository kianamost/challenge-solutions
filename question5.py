# function to check if input contains only letters and spaces
def is_valid_input(text):
    return all(word.isalpha() for word in text.split())

# function to sort words alphabetically and return as a sentence
def sort_sentence_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return " ".join(sorted_words)

# keep asking for valid input
while True:
    user_input = input("Enter a sentence (letters and spaces only): ")
    if is_valid_input(user_input):
        break
    else:
        print("Error: Only letters and spaces are allowed. Try again.")

# call the function and print the result
result = sort_sentence_alphabetically(user_input)
print(result)
