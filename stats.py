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

def get_alpha_freq(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            char_list.append({key:char_dict[key]})
    char_list.sort(reverse=True, key=lambda x:list(x.values())[0])
    return char_list
