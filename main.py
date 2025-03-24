from stats import get_num_words, get_num_chars, sorted_dict
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_num_chars = sorted_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_num_chars:
        if i["character"].isalpha():
            print(f"{i['character']}: {i['count']}")
    print("============= END ===============")


main()
