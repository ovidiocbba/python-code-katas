# https://www.codewars.com/kata/565b112d09c1adfdd500019c/train/python
def nth_char(words):
    cont = 0
    result = ""
    for word in words:
        result += word[cont]
        cont += 1
    return result
