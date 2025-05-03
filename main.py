# Bookbot

# Imports
import sys

# Checking sys.argv
if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Importing functions from stats.py
from stats import number_of_words, number_of_characters, sort_char

# Function for main program execution
def main():

    num_words = number_of_words()
    char_counts = number_of_characters()
    sorted_char = sort_char(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_char:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

# Main function to execute the program
if __name__ == "__main__":
    main()