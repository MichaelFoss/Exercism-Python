import math

def triplets_with_sum(number):
    # c can be at most half the number - 1,
    # because b has to be the other half
    max_c = number // 2 + 1
    triplets: list[list[int]] = []
    a: int = 3
    b: int = max_c - 1
    while a < b:
        c: int = number - a - b
        # Assign these to variables
        # so we don't have to recalc
        # in the elif statement
        a_squared: int = a * a
        b_squared: int = b * b
        c_squared: int = c * c
        if a_squared + b_squared == c_squared:
            triplets.append([a, b, c])
            # We know that if this is a triplet,
            # a & b are unique pairs and so we can skip both
            a += 1
            b -= 1
        # Look both ways to reduce
        # time spent reviewing potential triplets
        elif a_squared + b_squared > c_squared:
            b -= 1
        else: # a_squared + b_squared < c_squared:
            a += 1
    return triplets
