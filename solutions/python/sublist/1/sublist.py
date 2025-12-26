"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def is_superlist(list_one: list, list_two: list) -> bool:
    # list_one: list - must have length greater than list_two
    # list_two: list - must have length less than list_two
    for index, _value in enumerate(list_one):
        list_one_index = index
        list_two_index = 0
        is_contiguous = True
        while (list_one_index < len(list_one) and
               list_two_index < len(list_two) and
               is_contiguous):
            if list_one[list_one_index] != list_two[list_two_index]:
                is_contiguous = False
            else:
                list_one_index += 1
                list_two_index += 1
        if is_contiguous:
            return True
    return False

def sublist(list_one: list, list_two: list) -> int:
    if len(list_one) == len(list_two):
        for index, _value in enumerate(list_one):
            if list_one[index] != list_two[index]:
                return UNEQUAL
        return EQUAL
    else:
        if len(list_two) > len(list_one):
            if sublist(list_two, list_one) == SUPERLIST:
                return SUBLIST
            else:
                return UNEQUAL
        else:
            if is_superlist(list_one, list_two):
                return SUPERLIST
            else:
                return UNEQUAL