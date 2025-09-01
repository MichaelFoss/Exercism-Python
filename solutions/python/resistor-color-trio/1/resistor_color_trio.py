COLORS: list[str] = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
]

def get_value(color: str) -> int:
    if not color in COLORS:
        raise ValueError(f'{color} is not a valid color')
    return COLORS.index(color)

def get_suffix(value: int) -> str:
    suffix: str
    offset: int
    if value  == 0:
        offset = 1
    else:
        offset = 0
    if value < 3:
        suffix = 'ohms'
    elif value < 6:
        suffix = 'kiloohms'
    elif value < 9:
        suffix = 'megaohms'
    elif value < 12:
        suffix = 'gigaohms'
    else:
        raise ValueError(f'{value} has no valid suffix')
    zeros = '0' * (value % 3 - offset)
    return f'{zeros} {suffix}'

def label(colors: list[str]) -> int:
    if len(colors) < 3:
        raise ValueError('Resistor must be at least 3 colors')
    value_1: int = get_value(colors[0])
    value_2: int = get_value(colors[1])
    value: int
    zeros_value: int = get_value(colors[2])
    suffix: str
    if value_2 == 0:
        if value_1 == 0:
            return '0 ohms'
        zeros_value += 1
        value = value_1
    else:
        value = value_1 * 10 + value_2
    suffix = get_suffix(zeros_value)

    return f'{str(value)}{suffix}'
