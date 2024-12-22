def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"There are {word_count} words in {book_path}")
    print(f"The character counts for each letter are:\n{char_count}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    characters = {}
    for char in text.lower():
        if not char in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


main()