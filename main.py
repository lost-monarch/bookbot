from stats import word_count
from stats import character_count
from stats import char_sort
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    character_dict = character_count(get_book_text(sys.argv[1]))

    words = word_count(get_book_text(sys.argv[1]))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for i in char_sort(character_dict):
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

main()
