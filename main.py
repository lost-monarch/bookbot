from stats import word_count
from stats import character_count
from stats import char_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    character_dict = character_count(get_book_text("frankenstein.txt"))

    words = word_count(get_book_text("frankenstein.txt"))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"found {words} total words")
    print("--------- Character Count -------")
    
    for i in char_sort(character_dict):
        if i["char"].isalpha():
            print(f"{i['char']} : {i['num']}")
            
    print("============= END ===============")
    
main()
