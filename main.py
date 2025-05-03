from stats import number_of_words, number_of_characters, sort_char

def main():

    num_words = number_of_words()
    char_counts = number_of_characters()
    sorted_char = sort_char(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_char:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

if __name__ == "__main__":
    main()