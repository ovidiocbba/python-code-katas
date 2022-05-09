def amount_of_pages(summary):
    total_page = ""
    for number in range(1, summary + 1):
        total_page += str(number)
        if len(total_page) == summary:
            return number
