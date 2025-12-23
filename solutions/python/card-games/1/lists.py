"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    if len(hand) == 0:
        return 0
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    if len(hand) == 0:
        return True
    avg = card_average(hand)
    if (hand[0] + hand[-1]) / 2 == avg:
        return True
    if hand[int(len(hand) / 2)] == avg:
        return True
    return False

def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    if len(hand) <= 1:
        return False

    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    for _index, value in enumerate(hand):
        if _index % 2 == 0:
            even_sum += value
            even_count += 1
        else:
            odd_sum += value
            odd_count += 1
    return even_sum / even_count == odd_sum / odd_count


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if len(hand) == 0:
        return []

    new_hand = hand[:]
    if new_hand[-1] == 11:
        new_hand[-1] = 22
    return new_hand
        
