def dont_give_me_five(start, end):
    result = []
    for value in range(start, end + 1):
        if "5" not in str(value):
            result.append(value)
    return len(result)
