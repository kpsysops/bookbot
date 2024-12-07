def main():
    book_content = grab_a_book("books/frankenstein.txt")
    words = count_words(book_content)
    characters = count_characters(book_content)
    #print(characters.items())
    raport(words,characters)


def count_words(book_content):
    words = book_content.split()
    return len(words) 


def count_characters(book_content):
    chars = {}
    for c in book_content: # char-by-char
        lower_char = c.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars
  
    
def sort_on(dict):
    key_list = []
    for d in dict:
        key_list.append(dict[d])
    return key_list

def raport(words, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    list_characters = []
    for key in characters:
        if key.isalpha():
            list_characters.append({key: characters[key]})
    list_characters.sort(reverse=True, key=sort_on)
    for item in list_characters:
        for char in item:
            print(f"The '{char}' character was found {item[char]} times")
    print("--- End report ---")
    pass

def grab_a_book(path):
    with open(path) as f:
        return f.read()


main()


