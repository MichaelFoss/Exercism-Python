import math

DARTBOARD_RADIUS_OUTER = 10
DARTBOARD_RADIUS_MIDDLE = 5
DARTBOARD_RADIUS_INNER = 1
DARTBOARD_SCORE_OUTER = 1
DARTBOARD_SCORE_MIDDLE = 5
DARTBOARD_SCORE_INNER = 10

def get_distance_from_center(x: int, y: int):
    # According to Pythagoras, a²+b²=c²,
    # where a and b are the two shorter sides of a triangle
    # and c is the longest side.
    # 
    # By forming a right triangle with the short sides
    # of length x and y, we can be sure that there will be
    # a long side (so long as x != 0 and y != 0).
    # If the long side is treated as a vector
    # pointing away from the origin (the center of the dartboard),
    # we can get the length of the vector and determine
    # how far the dart is from the center.
    # 
    # Of course, if x = 0 or y = 0, the distance is trivial.
    if x == 0:
        return abs(y)
    if y == 0:
        return abs(x)
    return math.sqrt(x ** 2 + y ** 2)

def score(x: int, y: int):
    distance = get_distance_from_center(x, y)
    if distance <= DARTBOARD_RADIUS_INNER:
        return DARTBOARD_SCORE_INNER
    if distance <= DARTBOARD_RADIUS_MIDDLE:
        return DARTBOARD_SCORE_MIDDLE
    if distance <= DARTBOARD_RADIUS_OUTER:
        return DARTBOARD_SCORE_OUTER
    return 0
