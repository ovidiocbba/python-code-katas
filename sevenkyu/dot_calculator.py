import operator

operations = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "//": operator.floordiv}


def calculator(txt):
    values = txt.split()
    x = len(values[0])
    operation = values[1]
    y = len(values[-1])
    result = operations[operation](x, y)
    string_result = ""
    for x in range(0, result):
        string_result += "."
    return string_result

