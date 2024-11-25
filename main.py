def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_list = split(text)
    word_count = len(word_list)
    lowered_text = text.lower()
    character_dict = get_characters(lowered_text)
    alpha_chars = alpha_dict(character_dict)
    print(report(book_path, word_count, alpha_chars))


    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def split(text):
    words = text.split()
    return words

def get_characters(text):
    characters = {}
    for letter in text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def alpha_dict(character_dict):
    new_dict = {}
    for key, value in character_dict.items():
        if key.isalpha():
            new_dict[key] = value
    return new_dict

def sort_on(alpha_dict):
    return alpha_dict["num"]


def report(book_path, word_count, alpha_chars):
    sorted_chars = sorted(alpha_chars.items(), key=lambda item: item[1], reverse=True)
    char_report = "\n".join([f"The '{char}' character was found {count} times" for char, count in sorted_chars])
    
    return f"""--- Begin report of {book_path} ---
{word_count} words found in the document

{char_report}

--- End report ---
"""

           
main()
