# Globals for the directions
# Change the values as you see fit
SOUTH = 0
WEST = 1
NORTH = 2
EAST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
        return

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "L":
                self.direction = (self.direction + 3) % 4
            elif instruction == "R":
                self.direction = (self.direction + 1) % 4
            elif instruction == "A":
                if self.direction % 2 == 0:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + self.direction - 1)
                else:
                    self.coordinates = (self.coordinates[0] + self.direction - 2, self.coordinates[1])
        return
