import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionaries



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    full_text = get_book_text(path)
    count = count_characters(full_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(full_text)} total words")
    print("--------- Character Count -------")
    sorted_dict = sort_dictionaries(count)
    for char in sorted_dict:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
