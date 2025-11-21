import sys
from stats import get_num_words, get_character_stats, sort_stat_dictionary

def get_book_text(file_path): 
    with open(file_path) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    BOOK_PATH = sys.argv[1]

    book_content = get_book_text(BOOK_PATH)
    char_count = sort_stat_dictionary(get_character_stats(book_content))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOK_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_content)} total words")
    print("--------- Character Count -------")
    for char_dict in char_count:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
 
main()