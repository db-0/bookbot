from stats import get_word_count
import sys


def main():
    if len(sys.argv) != 2:
        print(" Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
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
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in chars:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()