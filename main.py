def main():
    book_path = "./books/frankenstein.txt"
    contents = get_book_contents(book_path)
    # wc = get_word_count(contents)
    character_count = get_character_count(contents)
    # print(character_count)
    print_letter_report(character_count)

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    character_dict = dict()
    for char in text:
        lowered = char.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict

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
