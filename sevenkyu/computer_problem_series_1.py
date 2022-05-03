def save(sizes, hd):
    total = 0
    cont = 0
    for value in sizes:
        if value > hd or total > hd:
            break
        elif total <= hd:
            total += value
            cont += 1
            if total > hd:
                cont -= 1
    return cont
