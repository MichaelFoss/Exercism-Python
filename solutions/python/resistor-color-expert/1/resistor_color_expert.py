from typing import Dict

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

TOLERANCES: Dict[str, float] = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
}

def get_text_value(value: int) -> str:
    ohm_suffices: Dict[int, str] = {
        9: 'giga',
        6: 'mega',
        3: 'kilo',
    }
    ohm_suffix: str = ''
    float_value: float = float(value)
    for power_of_10 in ohm_suffices:
        if ohm_suffix == '' and value >= (10 ** power_of_10):
            ohm_suffix = ohm_suffices[power_of_10]
            float_value = value / 10 ** power_of_10
    # Convert to string, dropping useless trailing zeros
    text_value: str = str(float_value)
    while text_value.endswith('0'):
        text_value = text_value[:-1]
    if text_value.endswith('.'):
        text_value = text_value[:-1]
    return f'{text_value} {ohm_suffix}ohms'

def resistor_label(colors):
    band_count: int = len(colors)
    if band_count == 1:
        if colors[0] == 'black':
            return '0 ohms'
        else:
            raise ValueError('Single-band resistors can only be black')
    if band_count < 4:
        raise ValueError('Resistors must have 1, 4, or 5 bands')
    # Simply ignore bands past 5

    tolerance_color: str = colors[-1]
    if tolerance_color not in TOLERANCES:
        raise ValueError(f'{tolerance_color} is not a valid tolerance color')
    tolerance: float = TOLERANCES[tolerance_color]

    multiplier_color: str = colors[-2]
    if multiplier_color not in COLORS:
        raise ValueError(f'{color} is not a valid multiplier color')
    multiplier: int = int(COLORS.index(colors[-2]))

    DIGITS_COUNT = len(colors) - 2
    value: int = 0
    digit_index: int = -3
    while digit_index * -1 <= DIGITS_COUNT + 2:
        color: str = colors[digit_index]
        if color not in COLORS:
            raise ValueError(f'{color} is not a valid resistor value color')
        value += COLORS.index(color) * 10 ** (digit_index * -1 - 3)
        digit_index -= 1
    value *= 10 ** multiplier

    text_value = get_text_value(value)
    return f'{text_value} ±{str(tolerance)}%'
