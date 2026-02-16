def get_num_of_digits(number):
    return len(str(number))

def is_armstrong_number(number):
    if (number < 10):
        return True
    digits = get_num_of_digits(number)
    sum = 0
    # Convert to string to access individual numbers
    number_str = str(number)
    for digit_index in range(0, digits):
        # Get individual digit
        digit = int(number_str[digit_index])
        # Calc added sum
        sum += digit ** digits
    return sum == number
