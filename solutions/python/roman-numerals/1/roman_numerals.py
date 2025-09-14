ROMAN_NUMERALS: list[list[tuple[int, str]]] = [
    [
        (1, 'I'),
        (5, 'V'),
    ],
    [
        (10, 'X'),
        (50, 'L'),
    ],
    [
        (100, 'C'),
        (500, 'D'),
    ],
    [
        (1000, 'M'),
        (5000, '?'),
    ],
]

def roman(number):
    if number not in range(1, 4000):
        raise ValueError('number must be between 1 and 3999')
    numerals: str = ''
    pair_index: int = -1
    pair: list[tuple[int, str]] = None
    while number > 0:
        pair_index += 1
        pair = ROMAN_NUMERALS[pair_index]
        numeral: str = ''
        first_pair = pair[0]
        second_pair = pair[1]

        digit = number % 10
        number = number // 10

        # 1-3
        if digit in range(1, 4):
            numeral += first_pair[1] * digit
        # 4, 9 (for smaller letter of compound digits)
        elif digit in [4, 9]:
            numeral += first_pair[1]
        # 4-8 (for larger letter of compound digits)
        if digit in range(4, 9):
            numeral += second_pair[1]
        # 9 (for larger letter of compound digits)
        elif digit == 9:
            # The next group's first pair's letter
            numeral += ROMAN_NUMERALS[pair_index + 1][0][1]
        # 6-8
        if digit in range(6, 9):
            numeral += first_pair[1] * (digit - 5)
        numerals = numeral + numerals
    return numerals
