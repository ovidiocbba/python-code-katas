def max_diff(lst):
    lst.sort()
    if len(lst) > 0:
        largest = lst[-1]
        smallest = lst[0]
        result = largest - smallest
    else:
        result = 0
    return result
