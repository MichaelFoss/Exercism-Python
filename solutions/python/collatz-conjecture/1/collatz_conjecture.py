def steps(number):
    count = 0
    if (number < 1):
        raise ValueError('Only positive integers are allowed')
    while (number != 1):
        isEven = number % 2 == 0
        if (isEven):
            number /= 2
        else:
            number = number * 3 + 1
        count += 1
    return count
