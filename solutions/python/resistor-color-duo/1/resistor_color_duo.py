COLORS = [
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

def color_value(color: str) -> int:
    if color not in COLORS:
        raise ValueError(f'{color} is not a valid color')
    return COLORS.index(color)

def value(colors: list[str]) -> int:
    if len(colors) == 0:
        return 0
    if len(colors) == 1:
        return color_value(colors[0])
    return color_value(colors[0]) * 10 + color_value(colors[1])
