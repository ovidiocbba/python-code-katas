def part_list(arr):
    result_list = []
    for index in range(1, len(arr)):
        first_part = ' '.join(arr[0:index])
        second_part = ' '.join(arr[index:])
        tuple_value = first_part, second_part
        result_list.append(tuple_value)
    return result_list
