def palindrome(num):
    if type(num) == str or int(num) < 0:
        return "Not valid"
    else:
        original_list = list(str(num))
    return original_list[::-1] == original_list
