from stats import get_word_count
from stats import get_character_count 
from stats import get_alpha_freq
def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    character_count = get_character_count(contents)
    word_count = get_word_count(contents)
    print_report(book_path, word_count, get_alpha_freq(get_character_count(contents)))

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def print_report(book_loc, word_count, character_dict_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_loc}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char_entry in character_dict_list:
        k, v = next(iter(char_entry.items()))
        print(f'{k}: {v}')
    print('============= END ===============')

if __name__ == "__main__":
    main()
