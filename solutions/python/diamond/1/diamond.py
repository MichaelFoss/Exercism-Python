def get_middle_row(letter: str) -> str:
    letter_number: int = ord(letter) - ord('A')
    middle: str = ''
    middle += letter
    middle += ' ' * (letter_number * 2 - 1)
    middle += letter
    return middle

def rows(letter):
    if (letter == 'A'):
        return ['A']
    lines: list[str] = []
    # Normalize the letter: A = 0, B = 1, etc.
    letter_number: int = ord(letter) - ord('A')
    lines.append(' ' * letter_number + 'A' + ' ' * letter_number)
    4 - (4 - 2) + 1
    for ch_index in range(1, letter_number):
        current_letter: str = chr(ord('A') + ch_index)
        # Calculate the paddings for the left part
        # of the line, in total spaces.
        # 
        # For example, for rows('E') line 'C',
        # the left ('°') and right ('•') paddings
        # are '°°C•..C..', yielding the following:
        # { 'left': '  ', right: ' ' }
        left_paddings = {
            'left': ' ' * (letter_number - ch_index),
            'right': ' ' * (ch_index - 1),
        }
        left: str = left_paddings['left'] + current_letter + left_paddings['right']
        # Right is simply left reversed
        right: str = left[::-1]
        lines.append(left + ' ' + right)
    # Copy the ascending lines into a new output
    output: list[str] = lines[:]
    # Calculate the middle
    output += [get_middle_row(letter)]
    # Copy the descending lines
    lines.reverse()
    output += lines
    return output
