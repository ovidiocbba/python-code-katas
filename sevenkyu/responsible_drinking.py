def hydrate(drink_string):
    list_values = drink_string.split()
    result = 0
    for value in list_values:
        if value.isnumeric():
            result += int(value[0])
    if result == 1:
        return str(result) + " glass of water"
    else:
        return str(result) + " glasses of water"
