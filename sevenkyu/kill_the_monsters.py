def kill_monsters(health, monsters, damage):
    hits = 0
    max_hits = 0
    for index in range(0, monsters):
        if max_hits == 3:
            max_hits = 0
            hits += 1
        max_hits += 1
    damage_total = damage * hits
    health -= damage_total
    if health <= 0:
        return "hero died"
    return f"hits: {hits}, damage: {damage_total}, health: {health}"
