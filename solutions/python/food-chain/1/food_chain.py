ANIMALS: list[tuple] = [
    ('fly', '', 'fly'),
    ('spider', 'It wriggled and jiggled and tickled inside her.', 'spider that wriggled and jiggled and tickled inside her'),
    ('bird', 'How absurd to swallow a bird!', 'bird'),
    ('cat', 'Imagine that, to swallow a cat!', 'cat'),
    ('dog', 'What a hog, to swallow a dog!', 'dog'),
    ('goat', 'Just opened her throat and swallowed a goat!', 'goat'),
    ('cow', "I don't know how she swallowed a cow!", 'cow'),
    ('horse', "She's dead, of course!", '')
]

def recite(start_verse, end_verse):
    lines: list[str] = []
    if start_verse < 1 or end_verse > 8 or end_verse < start_verse:
        raise ValueError('Start/end verse error: 1 <= start_verse <= end_verse <= 8')
    for line_num in range(start_verse, end_verse + 1):
        (animal_name, line_two, caught_animal_name) = ANIMALS[line_num - 1]
        lines.append(f"I know an old lady who swallowed a {animal_name}.")
        if len(line_two) > 0:
            lines.append(line_two)
        # If the animal can't be caught,
        # the lady's dead and we should stop singing 🪦
        if caught_animal_name == "":
            break
        for smaller_animal_num in range(line_num - 1, 0, -1):
            line: str = "She swallowed the [[BIGGER]] to catch the [[SMALLER]]."
            bigger_animal_name: string = ANIMALS[smaller_animal_num][0]
            smaller_animal_name: string = ANIMALS[smaller_animal_num - 1][2]
            line = line.replace('[[BIGGER]]', bigger_animal_name)
            line = line.replace('[[SMALLER]]', smaller_animal_name)
            lines.append(line)
        lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        # Prep for the next verse if we're singing it
        if line_num < end_verse:
            lines.append("")
    print("\n".join(lines))
    return lines
