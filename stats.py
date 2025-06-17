def count_words(text):
    split_text = len(text.split())
    return split_text

def count_characters(text):
    characters = {}
    for character in text:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            characters[character.lower()] += 1
    return characters

def sort_on(dict):
    return dict["num"]


def sort_dictionaries(dictionary):
    sorted_dictionaries = []
    for char,num in dictionary.items():
        dicts = {"char":char, "num": num}
        sorted_dictionaries.append(dicts)
    sorted_dictionaries.sort(reverse=True, key=sort_on)
    return sorted_dictionaries