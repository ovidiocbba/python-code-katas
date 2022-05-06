def battle(x, y):
    alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                "X": 24, "Y": 25, "Z": 26}
    x_value = 0
    y_value = 0
    result = ""
    for value in str(x):
        x_value += alphabet.get(value)
    for value in str(y):
        y_value += alphabet.get(value)
    if x_value == y_value:
        result = "Tie!"
    elif x_value > y_value:
        result = x
    elif y_value > x_value:
        result = y
    return result
