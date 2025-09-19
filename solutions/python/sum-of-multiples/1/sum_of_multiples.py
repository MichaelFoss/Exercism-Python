def get_magical_item_multiples(magical_item: int, level: int) -> set[int]:
    multiples: set[int] = set()
    if magical_item == 0:
        return multiples
    next_multiple: int = magical_item
    while next_multiple < level:
        multiples.add(next_multiple)
        next_multiple += magical_item
    return multiples

def sum_of_multiples(level: int, magical_items: list[int]) -> int:
    all_multiples: set[int] = set()
    for magical_item in magical_items:
        current_multiples: set[int] = get_magical_item_multiples(magical_item, level)
        all_multiples = all_multiples | current_multiples

    sum: int = 0
    for multiple in all_multiples:
        sum += multiple
    return sum
