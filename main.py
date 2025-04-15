import sys
from stats import count, count_chars, get_book_text, chars_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)
    print("----------- Word Count ----------")
    num_words = count(path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = count_chars(text)
    sorted_chars = chars_to_sorted_list(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")
    print("============= END ===============")


main()