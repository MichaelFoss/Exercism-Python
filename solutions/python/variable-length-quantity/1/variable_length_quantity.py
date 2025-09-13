import math

IS_TERMINATING_SEQUENCE: int = 0

def to_binary(num: int) -> list[int]:
    bin_num: list[int] = []
    while True:
        bin_num = [num % 2] + bin_num
        num = num >> 1
        if num == 0:
            break
    return bin_num

def from_binary(bin_num: list[int]) -> list[int]:
    num: int = 0
    for (index, val) in enumerate(reversed(bin_num)):
        num += val * 2 ** index
    return num

"""
Converts a single int
to a uint 0-127 list, VLQ-encoded.
"""
def encode_single(number: int) -> list[int]:
    isOutOfRange: bool = number < 0
    if isOutOfRange:
        raise ValueError("numbers must be single unsigned integers")

    encoding: list[int] = []

    # Convert the number to binary
    number_bin: list[int] = to_binary(number)

    # Add leading zeros to ensure the number is groups of 7 bits
    number_bin = [0] * ((7 - (len(number_bin) % 7)) % 7) + number_bin

    # Iterate over each group of 7 bits
    bit_group_length: int = int(len(number_bin) / 7)
    for bit_group_index in range(0, bit_group_length):
        # Extract the bit group from the sequence
        start_bit: int = bit_group_index * 7
        end_bit: int = bit_group_index * 7 + 7
        flag: int = 0 if bit_group_index == bit_group_length - 1 else 1
        bit_group: list[int] = [flag] + number_bin[start_bit:end_bit]

        # Encode the bit group and add it to the encoding
        encoded_part: int = from_binary(bit_group)
        encoding.append(encoded_part)

    # If 0 was passed, we didn't loop, and the array is still empty
    if len(encoding) == 0:
        return [0]

    return encoding


def encode(numbers: list[int]) -> list[int]:
    encoding: list[int] = []
    for number in numbers:
        encoding += encode_single(number)
    return encoding


"""
Converts a list of VLQ-encoded decimal uints
in uint int 0-127 format back to the original
list of decimal uints.
"""
def decode(bytes_: list[int]) -> list[int]:
    numbers: list[int] = []
    current_number_sequence: list[int] = []
    for num in bytes_:
        # If the number is not 0-127, throw an error
        if num < 0 or num > 0xFF:
            raise ValueError('incomplete sequence')

        # Get the binary representation of the number
        num_in_bits: list[int] = to_binary(num)

        # Pad the value to exactly 8 bits
        num_in_bits = [0] * (8 - len(num_in_bits)) + num_in_bits

        # Split the sequence part into a flag and data
        flag: int = num_in_bits[0:1][0]
        data: list[int] = num_in_bits[1:8]

        # Add the data to the current number
        current_number_sequence += data

        # If this is the end of the current number,
        # calculate the value and reinitialize the current number
        if flag == IS_TERMINATING_SEQUENCE:
            new_number: int = from_binary(current_number_sequence)
            numbers.append(new_number)
            current_number_sequence = []

    # If we have any data left, there was a non-terminating number
    # at the end and this whole decoding should fail
    if len(current_number_sequence) > 0:
        raise ValueError('incomplete sequence')
    return numbers
