from stats import word_count
from stats import character_count
from stats import char_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    character_dict = character_count(get_book_text("books/frankenstein.txt"))

    words = word_count(get_book_text("books/frankenstein.txt"))

    print(f"{words} words in the document")
    #print(character_dict)
    print(char_sort(character_dict))

main()
