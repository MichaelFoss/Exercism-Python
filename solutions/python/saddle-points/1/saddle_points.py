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

def get_ranges(matrix: list[list[int]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    # Ranges of shortest and tallest trees in rows & cols
    row_ranges: list[tuple[int, int]] = []
    col_ranges: list[tuple[int, int]] = []
    for row in matrix:
        row_heights: list[int] = sorted(list(set(row)))
        row_ranges.append((row_heights[0], row_heights[-1]))
    first_row = matrix[0]
    for col_index in range(0, len(first_row)):
        col_heights: list[int] = []
        for row_index in range(0, len(matrix)):
            col_heights.append(matrix[row_index][col_index])
        col_heights = sorted(list(set(col_heights)))
        col_ranges.append((col_heights[0], col_heights[-1]))
    return (row_ranges, col_ranges)

def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    if len(matrix) == 0:
        return []
    if is_irregular(matrix):
        raise ValueError("irregular matrix")
    (row_ranges, col_ranges) = get_ranges(matrix)
    acceptable_trees: list[dict[str, int]] = []
    for row_index in range(0, len(matrix)):
        for col_index in range(0, len(matrix[row_index])):
            tree_height: int = matrix[row_index][col_index]
            min_col_tree_height = col_ranges[col_index][0]
            max_row_tree_height = row_ranges[row_index][1]
            if tree_height == min_col_tree_height == max_row_tree_height:
                acceptable_trees.append({
                    "row": row_index + 1,
                    "column": col_index + 1
                })
    print(acceptable_trees)
    return acceptable_trees