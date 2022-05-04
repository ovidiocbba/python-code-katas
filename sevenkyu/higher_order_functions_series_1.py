def count_developers(lst):
    result = 0
    for value in lst:
        if value["language"] == "JavaScript" and value["continent"] == "Europe":
            result += 1
    return result
