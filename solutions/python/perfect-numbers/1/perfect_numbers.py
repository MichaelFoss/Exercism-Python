def get_aliquot_sum(number: int):
    sum = 0
    for sub_number in range(1, int(number / 2) + 1):
        if number % sub_number == 0:
            sum += sub_number
    return sum

def classify(number: int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    aliquot_sum = get_aliquot_sum(number)
    if aliquot_sum < number:
        return 'deficient'
    if aliquot_sum > number:
        return 'abundant'
    return 'perfect'
