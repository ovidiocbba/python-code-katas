def find_position(element):
    translation = [['A', 'B', 'C', 'D', 'E'],
                   ['F', 'G', 'H', 'I', 'J'],
                   ['L', 'M', 'N', 'O', 'P'],
                   ['Q', 'R', 'S', 'T', 'U'],
                   ['V', 'W', 'X', 'Y', 'Z']]
    if element == 'K':
        return 1, 3
    for i in range(len(translation)):
        for j in range(len(translation[i])):
            if translation[i][j] == element:
                return i + 1, j + 1


def tap_code_translation(text):
    code_translation = ""
    for value in text.upper():
        a, b = find_position(value)
        code_translation += "".join(["." for _ in range(0, a)]) + " " + "".join(["." for _ in range(0, b)]) + " "
    return code_translation[:-1]
