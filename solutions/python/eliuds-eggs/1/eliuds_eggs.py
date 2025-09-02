EGG: str = '1'

def egg_count(display_value: int) -> int:
    # This works too, but might be cheating due to the count method:
    # return str(bin(display_value))[2:].count('1')

    spots: str = str(bin(display_value))[2:]
    count: int = 0
    for spot in spots:
        if spot == EGG:
            count += 1
    return count
