# Bookbot

from stats import get_num_words, get_num_chars, sort_dict

def main():

    num_chars = get_num_chars(get_book_text("books/frankenstein.txt"))
    sort_chars = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")
    print("--------- Character Count -------")
    for item in sort_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    
    return file_contents

main()