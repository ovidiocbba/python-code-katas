def filter_long_words(sentence, n):
    result = []
    for value in sentence.split():
        if len(value) > n:
            result.append(value)
    return result
