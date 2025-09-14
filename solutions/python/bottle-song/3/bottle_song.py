NUM_WORDS: dict[int, str] = {
    0: 'No',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
}

def recite(start, take=1):
    if start <= 0:
        raise ValueError("start must be at least 1")
    if take < 1:
        raise ValueError("take must be at least 1")

    bottles: int = start
    verse: list[str] = []
    for verse_num in range(1, take + 1):
        current_verse: list[str] = []
        current_verse.append(f"{NUM_WORDS[bottles]} green bottle{'s' if bottles != 1 else ''} hanging on the wall,")
        current_verse.append(current_verse[0])
        current_verse.append(f"And if one green bottle should accidentally fall,")

        # Take the bottle off the wall
        bottles -= 1
        if bottles < 0:
            bottles = 0

        current_verse.append(f"There'll be {NUM_WORDS[bottles].lower()} green bottle{'s' if bottles != 1 else ''} hanging on the wall.")

        verse = verse + current_verse

        # Add space in preparation for next verse
        is_last_verse: bool = verse_num == take
        if not is_last_verse:
            verse.append('')

    return verse