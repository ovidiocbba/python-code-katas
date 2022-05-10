def digital_root(n):
    status = True
    value = n
    result = 0
    while status:
        result = root(value)
        if len(result) == 1:
            status = False
        else:
            value = int(result)
    return int(result)


def root(n):
    total = 0
    for value in str(n):
        total += int(value)
    return str(total)
