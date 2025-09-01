PRECISION = 10

def square_root(number: int) -> int:
    """
    number: int - The number to get the root of (must be a perfect square!)
    returns: The square root of the number
    """

    estimate: float = 0.5 * 10 ** 2
    for iteration_count in range(1, PRECISION):
        estimate = 0.5 * (estimate + number / estimate)

    return int(estimate)