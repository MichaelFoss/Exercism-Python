def has_valid_digits(digits: list[int], input_base: int) -> bool:
    for digit in digits:
        if not (0 <= digit < input_base):
            return False
    return True

def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not has_valid_digits(digits, input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if len(digits) == 0:
        return [0]

    number = 0
    # input_base --> base 10
    for index, digit in enumerate(reversed(digits)):
        number += digit * input_base ** index
    #  base 10 --> output_base
    new_digits: list[int] = []
    while number > 0:
        new_digits.insert(0, number % output_base)
        print(new_digits)
        number = int(number / output_base)

    if len(new_digits) == 0:
        return [0]
    return new_digits
