def is_valid(isbn):
    # Prettify the string
    isbn = isbn.strip().upper()

    # Make sure we have a long-enough string
    if len(isbn) < 10:
        return False

    # Confirm string starts with a number
    if not isbn[0:1].isdigit():
        return False

    # Confirm ends with a number or an X
    if isbn[-1] != 'X' and not isbn[-1].isdigit():
        return False

    # Strip all dashes, then
    # confirm has only digits and dashes in between
    dashless_isbn = isbn.replace('-', '')
    if not dashless_isbn[0:-1].isdigit():
        return False

    # Confirm number of digits/characters is accurate
    if len(dashless_isbn) != 10:
        return False

    # Create a list of characters
    chars = list(dashless_isbn)

    # Convert the list of characters into numbers
    if chars[-1] == 'X':
        chars[-1] = '10'
    numbers = [int(s) for s in chars]

    # Calculate the checksum
    checksum = 0
    for index in range(0, len(numbers)):
        checksum += numbers[index] * (10 - index)

    # Compare the checksum calculation to the expected value of 0
    return checksum % 11 == 0
