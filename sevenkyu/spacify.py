def spacify(string):
    result = ""
    for index in range(0, len(string)):
        result += string[index] + " "
    return result[:-1]