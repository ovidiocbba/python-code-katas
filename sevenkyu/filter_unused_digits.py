def unused_digits(*args):
    # Create a list from a String
    list_result = list("".join([str(value) for value in args]))
    list_result.sort()
    list_final = list(dict.fromkeys(list_result))
    list_final = [int(value) for value in list_final]
    difference = set(list_final).symmetric_difference(set([value for value in range(0, 10)]))
    return "".join([str(value) for value in difference])
