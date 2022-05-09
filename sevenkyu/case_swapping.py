def swap(string_):
    total = ""
    for character in string_:
        if character.isupper():
            total += character.lower()
        else:
            total += character.upper()
    return total
