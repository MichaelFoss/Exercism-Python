def valid_triangle(sides):
    valid_lengths = sides[0] > 0 and sides[1] > 0 and sides[2] > 0
    valid_shape_0 = sides[0] <= sides[1] + sides[2]
    valid_shape_1 = sides[1] <= sides[0] + sides[2]
    valid_shape_2 = sides[2] <= sides[0] + sides[1]
    valid_shape = valid_shape_0 and valid_shape_1 and valid_shape_2
    return valid_lengths and valid_shape

def equilateral(sides):
    all_sides_equal = sides[0] == sides[1] == sides[2]
    return valid_triangle(sides) and all_sides_equal

def isosceles(sides):
    two_sides_equal = sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
    return valid_triangle(sides) and two_sides_equal


def scalene(sides):
    no_sides_equal = sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
    return valid_triangle(sides) and no_sides_equal
