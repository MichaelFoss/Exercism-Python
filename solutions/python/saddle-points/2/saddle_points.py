def is_irregular(matrix: list[list[int]]) -> bool:
    # If rows exist but don't have cols, it's irregular
    row_len = len(matrix[0])
    if row_len == 0:
        return True
    # If the matrix has uneven row lengths, it's irregular
    first_row = matrix[0]
    row_len = len(first_row)
    for row in matrix:
        if len(row) != row_len:
            return True
    return False

def get_ranges(matrix: list[list[int]]) -> tuple[list[int], list[int]]:
    """
    Given a matrix, returns a tuple of two int lists
    containing each row's tallest tree and each
    column's shortest tree.
    """
    # Ranges of shortest and tallest trees in rows & cols
    tallest_trees_by_row: list[int] = []
    shortest_trees_by_column: list[int] = []
    for row in matrix:
        row_heights: list[int] = sorted(list(set(row)))
        tallest_trees_by_row.append(row_heights[-1])
    first_row = matrix[0]
    for col_index in range(0, len(first_row)):
        col_heights: list[int] = []
        for row_index in range(0, len(matrix)):
            col_heights.append(matrix[row_index][col_index])
        col_heights = sorted(list(set(col_heights)))
        shortest_trees_by_column.append(col_heights[0])
    return (tallest_trees_by_row, shortest_trees_by_column)

def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    if len(matrix) == 0:
        return []
    if is_irregular(matrix):
        raise ValueError("irregular matrix")
    (tallest_trees_by_row, shortest_trees_by_column) = get_ranges(matrix)
    acceptable_trees: list[dict[str, int]] = []
    for row_index in range(0, len(matrix)):
        for col_index in range(0, len(matrix[row_index])):
            tree_height: int = matrix[row_index][col_index]
            tallest_tree_height_in_row = tallest_trees_by_row[row_index]
            shortest_tree_height_in_col = shortest_trees_by_column[col_index]
            if tree_height == shortest_tree_height_in_col == tallest_tree_height_in_row:
                acceptable_trees.append({
                    "row": row_index + 1,
                    "column": col_index + 1
                })
    return acceptable_trees