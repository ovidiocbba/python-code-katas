def filter_list(new_list):
    result_list = []
    for value in new_list:
        if str(value).isdigit():
            if type(value) != str:
                result_list.append(value)
    return result_list
