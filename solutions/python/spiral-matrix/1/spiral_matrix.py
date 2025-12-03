UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def create_matrix(size):
    matrix = []
    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            matrix[i].append(0)
    return matrix

def spiral_matrix(size):
    if size == 1:
        return [[1]]
    matrix = create_matrix(size)
    dir = RIGHT
    x = 0
    y = 0
    for i in range(1, size * size + 1):
        print(f"{i}: {x},{y}")
        print(matrix)
        matrix[y][x] = i
        if dir == RIGHT:
            if x == size - 1 or x < size - 1 and matrix[y][x + 1] != 0:
                dir = DOWN
                y += 1
            else:
                x += 1
        elif dir == DOWN:
            if y == size - 1 or y < size - 1 and matrix[y + 1][x] != 0:
                dir = LEFT
                x -= 1
            else:
                y += 1
        elif dir == LEFT:
            if x == 0 or x > 0 and matrix[y][x - 1] != 0:
                dir = UP
                y -= 1
            else:
                x -= 1
        elif dir == UP:
            if y == 0 or y > 0 and matrix[y - 1][x] != 0:
                dir = RIGHT
                x += 1
            else:
                y -= 1
    return matrix
