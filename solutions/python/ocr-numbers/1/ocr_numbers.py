ALL_DIGIT_GLYPHS = [
  ' _     _  _     _  _  _  _  _ ',
  '| |  | _| _||_||_ |_   ||_||_|',
  '|_|  ||_  _|  | _||_|  ||_| _|',
]

def build_digits_lines() -> list[list[str]]:
    lines: list[list[str]] = []
    for number in range(0, len(ALL_DIGIT_GLYPHS[0]), 3):
        digit: list[str] = []
        for line_number in range(0, 3):
            digit.append(ALL_DIGIT_GLYPHS[line_number][number:number + 3])
        lines.append(digit)
    return lines

# All digits' glyphs; each digit is the index of the List,
# and the glyph is a 3x3 ASCII char (last line of 3x4
# is always blank anyways, so it is removed).
DIGIT_GLYPHS: list[list[str]] = build_digits_lines()


# Given a row and column in the grid, gets the 3x3 slice.
# Does not check to see if it is in bounds or a valid glyph.
def get_glyph(input_grid: list[str], row: int, col: int) -> list[str]:
    glyph: list[str] = []
    for y in range(row, row + 3):
        line: str = input_grid[y][col:col + 3]
        glyph.append(line)
    return glyph


# Given a 3x3 glyph, returns the digit it represents,
# or '?' if it doesn't represent a digit.
def convert_glyph(glyph: list[str]) -> str:
    for digit, digit_glyph in enumerate(DIGIT_GLYPHS):
        if glyph == digit_glyph:
            return str(digit)
    return '?'


def convert(input_grid: list[str]) -> str:
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for line in input_grid:
        if len(line) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    conversion: str = ''
    # Scan the grid, left-to-right, top-to-bottom,
    # counting by glyph locations (the top-left most
    # character in each glyph)
    for row in range(0, len(input_grid), 4):
        if row != 0:
            conversion += ','
        for col in range(0, len(input_grid[row]), 3):
            glyph: list[str] = get_glyph(input_grid, row, col)
            digit: str = convert_glyph(glyph)
            conversion += digit
    return conversion

