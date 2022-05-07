def array_leaders(numbers):
    result = []
    for index in range(0, len(numbers)):
        sum_right_side = sum(numbers[index + 1:])
        if numbers[index] > sum_right_side:
            result.append(numbers[index])
    return result
