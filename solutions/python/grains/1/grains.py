def square(number):
    if (number < 1 or number > 64):
        raise ValueError('square must be between 1 and 64')
    return 2 ** (number - 1)


def total():
    def calc(number, grains):
        if (number == 0):
            return grains
        new_grains = grains + square(number)
        return calc(number - 1, new_grains)
    return calc(64, 0)
