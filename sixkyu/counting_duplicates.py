def duplicate_count(text):
    original_list = list(text.upper())
    diff_list = list(dict.fromkeys(original_list))
    duplicate = 0
    for value in diff_list:
        if original_list.count(value) > 1:
            duplicate += 1
    return duplicate
