import re


def fire_and_fury(tweet):
    is_valid = re.fullmatch('[EFIRUY]+', tweet)
    result_list = re.findall(r"(FURY|FIRE)", tweet)
    result_value = ""
    if len(result_list) == 0 or not(bool(is_valid)):
        return "Fake tweet."
    else:
        last = result_list[0]
        i = 0
        for index, value in enumerate(result_list):
            if value == last:
                i += 1
            elif value != last:
                result_value += result_string(last, i) + " "
                i = 1
                last = value
            if index == len(result_list) - 1:
                result_value += result_string(last, i)
    return result_value


def result_string(value, number):
    if value == "FURY":
        if number == 1:
            text = ""
        else:
            text = "really " * (number - 1)
        return f"I am {text}furious."
    elif value == "FIRE":
        if number == 1:
            text = ""
        else:
            text = "and you " * (number - 1)
        return f"You {text}are fired!"