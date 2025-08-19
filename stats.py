def word_count(book_content):
    word_count = 0
    words = book_content.split()
    for word in words:
        word_count += 1
    return word_count

def character_count(book_contents):
    character = {}
    lowercase = book_contents.lower()
    for char in lowercase:
        if char not in character:
            character[char] = 1
        else:
            character[char] += 1
    return character

def char_sort(book_contents):
    sorted = []
    for c in book_contents:
        char_count = {}
        if c.isalpha() == True:
            char_count["char"] = c
            char_count["num"] = book_contents[c]
            sorted.append(char_count)
        else:
            None
    def sort_on(items):
        return items["num"]
            
    sorted.sort(reverse=True, key=sort_on)    
    
    for items in sorted:
        print(f"{items['char']}: {items['num']}")
