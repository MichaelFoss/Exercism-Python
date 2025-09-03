EMPTY: str = ' '
FLOWER: str = '*'
VALID_SPACES: str = EMPTY + FLOWER

def is_valid_square(garden: list[str], x: int, y: int) -> bool:
    if x < 0 or y < 0:
        return False
    if y >= len(garden):
        return False
    if x >= len(garden[0]):
        return False
    return True

def get_flower_count(garden: list[str], row: int, col: int) -> int:
    count: int = 0
    # print(garden)
    for y in range(row - 1, row + 2):
        for x in range(col - 1, col + 2):
            # print(f'y = {y}, x = {x}')
            if x == col and y == row:
                continue
            if is_valid_square(garden, x, y):
                if garden[y][x:x + 1] == FLOWER:
                    count += 1
    return count

def is_valid(garden: list[str]) -> bool:
    line_length: int = None
    for garden_row in garden:
        if line_length == None:
            line_length = len(garden_row)
        elif len(garden_row) != line_length:
            return False
        for space in list(garden_row):
            if space not in VALID_SPACES:
                return False
    return True

def annotate(garden: list[str]) -> list[str]:
    if not is_valid(garden):
        raise ValueError("The board is invalid with current input.")
    if len(garden) == 0:
        return []
    garden_count: list[str] = []
    for row in range(0, len(garden)):
        garden_count.append('')
        for col in range(0, len(garden[row])):
            if garden[row][col:col + 1] == FLOWER:
                garden_count[row] += FLOWER
            else:
                count: int = get_flower_count(garden, row, col)
                if count == 0:
                    garden_count[row] += EMPTY
                else:
                    garden_count[row] += str(count)
    return garden_count

