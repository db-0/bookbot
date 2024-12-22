def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_count.sort(reverse=True, key=sort_on)
    print_report(book_path, word_count, char_count)


def sort_on(dict):
    return dict["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    chars = {}
    char_lod = []
    for c in text.lower():
        if c.isalpha():
            if not c in chars:
                chars[c] = 1
            else:
                chars[c] += 1
    for k,v in chars.items():
        char_lod.append({"char": k, "num": v})
    return char_lod


def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"There are {words} words in this document.\n")
    for dict in chars:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")
    print("--- End Report ---")


main()