def even_and_odd(n):
    even = ""
    odd = ""
    for value in str(n):
        if int(value) % 2 == 0 or value == "0":
            even += value
        else:
            odd += value
    if not odd:
        odd = "0"
    elif not even:
        even = "0"
    return int(even), int(odd)
