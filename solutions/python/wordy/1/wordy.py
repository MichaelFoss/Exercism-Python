from typing import Dict

PLUS = '+'
MINUS = '–'
MULTIPLY = '*'
DIVIDE = '/'
VALID_OPERATORS: str = f'{PLUS}{MINUS}{MULTIPLY}{DIVIDE}'
OPERATOR_MAPPING: Dict[str, str] = {
    'plus': PLUS,
    'minus': MINUS,
    'multiplied by': MULTIPLY,
    'divided by': DIVIDE,
}

def is_number(s: str) -> bool:
    if len(s) == 0:
        return False
    return s[0] == '-' and s[1:].isdigit() or s.isdigit()

def get_question_parts(question: str) -> list:
    if not question.startswith('What is ') or not question.endswith('?'):
        raise ValueError('syntax error')
    question = question[len('What is '):-1]
    for replacement in OPERATOR_MAPPING:
        operator = OPERATOR_MAPPING[replacement]
        question = question.replace(replacement, operator)
    question = question.replace('  ', ' ')
    question = question.replace('  ', ' ')
    question_parts = question.split(' ')
    parts: list = []

    for question_part in question_parts:
        if question_part in VALID_OPERATORS:
            parts.append(question_part)
        elif is_number(question_part):
            parts.append(int(question_part))
        else:
            raise ValueError('unknown operation')

    if len(parts) == 0:
        raise ValueError("syntax error")

    # Parts should be odd - starting with a number,
    # followed by 0 or more operator/number pairs
    if len(parts) % 2 != 1:
        raise ValueError('syntax error')

    # Check that all parts alternate between numbers and operators
    is_number_expected = True
    for part in parts:
        if is_number_expected:
            if not is_number(str(part)):
                raise ValueError('syntax error')
        if not is_number_expected:
            if str(part) not in VALID_OPERATORS:
                raise ValueError('syntax error')
        is_number_expected = not is_number_expected

    # If we made it this far, return the parts
    return parts

def do_math(val_1: int, val_2: int, operator: str) -> int:
    if operator == PLUS:
        return val_1 + val_2
    if operator == MINUS:
        return val_1 - val_2
    if operator == MULTIPLY:
        return val_1 * val_2
    if operator == DIVIDE:
        return val_1 / val_2
    raise ValueError(f'Unknown operator {operator}')

def answer(question):
    question_parts = get_question_parts(question)
    while len(question_parts) != 1:
        val_1: int = question_parts.pop(0)
        operator: str = question_parts.pop(0)
        val_2: int = question_parts.pop(0)
        result: int = do_math(val_1, val_2, operator)
        question_parts.insert(0, result)
    return question_parts[0]
