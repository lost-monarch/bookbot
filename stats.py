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
    for char in dict:
        if char.isalpha() == True:
            sorted.append(char: dict[char])
        else:
            None
    return sorted
