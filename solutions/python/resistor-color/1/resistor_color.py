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

def color_code(color):
    if not color in COLORS:
        raise ValueError(f'{color} is not a valid color')
    return COLORS.index(color)


def colors():
    return COLORS
