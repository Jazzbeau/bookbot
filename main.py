from stats import get_word_count
from stats import get_character_count 
def main():
    book_path = "./books/frankenstein.txt"
    contents = get_book_contents(book_path)
    # wc = get_word_count(contents)
    character_count = get_character_count(contents)
    word_count = get_word_count(contents)
    # print(character_count)
    # print_letter_report(character_count)
    print(f'{word_count} words found in the document')

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def print_letter_report(letter_dict):
    frequencies = []

    for letter, frequency in letter_dict.items():
        if letter.isalpha():
            frequencies.append((letter, frequency))
 
    # Sort by second value, frequency
    frequencies.sort(reverse=True, key=lambda x:x[1])

    # Print to stdout
    for value in frequencies:
        print(f"The '{value[0]}' character was found {value[1]} times")

    return 

# Execution

if __name__ == "__main__":
    main()
