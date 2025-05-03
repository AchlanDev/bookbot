# Bookbot Statistics Functions

# Imports
import sys

# Function to get the text from the book
def get_book_text(path):

    with open(path) as f:
        return f.read()

# Function to count the number of words in the book
def number_of_words():

    text = get_book_text(sys.argv[1])

    words = text.split()
    
    num_words = len(words)

    return num_words

# Function to count the number of characters in the book
def number_of_characters():

    text = get_book_text(sys.argv[1])
    char_counts = {}

    for char in text.lower():

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

# Function to set key for sorting
def sort_on(char_count):
    return char_count["num"]

# Function to sort the character counts
def sort_char(char_counts):

    filtered_char = {char: num for char, num in char_counts.items() if char.isalpha()}

    sorted_char = [{"char": char, "num": num} for char, num in filtered_char.items()]

    sorted_char.sort(reverse=True, key=sort_on)

    return sorted_char

