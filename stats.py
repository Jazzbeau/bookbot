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
