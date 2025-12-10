# Analyze the texts

def get_num_words(file_contents):
    split_words = file_contents.split()
    return len(split_words)

def get_num_chars(file_contents):

    counts = {}

    text = file_contents.lower()

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts

def sort_on(items):    
    return items["num"]

def sort_dict(counts):
    char_list = []

    for char, num in counts.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)
    return char_list