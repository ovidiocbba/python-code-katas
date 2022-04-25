def sum_of_minimums(numbers):
    total = 0
    for value in numbers:
        value.sort()
        total += value[0]
    return total
