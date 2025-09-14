def get_available_dominoes(target: int, dominoes: list[tuple[int, int]]) -> list[tuple[int, int]]:
    available_dominoes: list[tuple[int, int]] = []
    for domino in dominoes:
        if domino[0] == target:
            available_dominoes.append((domino[0], domino[1]))
        elif domino[1] == target:
            available_dominoes.append((domino[1], domino[0]))
    return available_dominoes

def can_chain(dominoes: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # No dominoes? Stop here.
    if len(dominoes) == 0:
        return []
    # One domino? Check to see if it's a doublet.
    if len(dominoes) == 1:
        is_doublet: bool = dominoes[0][0] == dominoes[0][1]
        if is_doublet:
            return dominoes
        else:
            return None

    # Initialize the search with a single domino for each search item
    search: list[tuple[list[tuple[int, int]], list[tuple[int, int]]]] = []
    for domino in dominoes:
        remaining_dominoes: list[tuple[int, int]] = dominoes.copy()
        remaining_dominoes.remove(domino)
        search.append(([domino], remaining_dominoes))

    # Keep searching until we find a valid chain
    # or we've exhausted the search
    while len(search) > 0:
        (path, remaining_dominoes) = search.pop()
        tail_domino: tuple[int, int] = path[-1]
        available_dominoes = get_available_dominoes(tail_domino[1], remaining_dominoes)
        for domino in available_dominoes:
            new_path: list[tuple[int, int]] = path.copy() + [domino]
            new_remaining_dominoes: list[tuple[int, int]] = remaining_dominoes.copy()
            if domino in new_remaining_dominoes:
                new_remaining_dominoes.remove(domino)
            else:
                new_remaining_dominoes.remove((domino[1], domino[0]))
            if len(new_remaining_dominoes) > 0:
                search.append((new_path, new_remaining_dominoes))
            else:
                is_path_wrapping: bool = new_path[0][0] == new_path[-1][1]
                if is_path_wrapping:
                    return new_path
    return None

    """
    Create a search list with:
        All dominos as initial paths
        All remaining dominos as possible pulls
    While search is not empty:
        Pull search item from end of list
        Create new search items based on all possible matches
        If a search item's path is full and start matches end (it wraps), return that value
        Add new search items to end of search list
    return None
        
    # Initized
    [ # list
        [ # tuple
            [[1, 2]], # list[tuple[int, int]]
            [[2, 3], [3, 1]]], # list[tuple[int, int]]
        ],
        [
            [[2, 3]],
            [[1, 2], [3, 1]],
        ],
        [
            [[3, 1]],
            [[1, 2], [2, 3]],
        ],
    ]
    # Pull 3, 1 from the back, find all connections,
    # then stick them all back at the end
    [
        [
            [[1, 2]], # list[tuple[int, int]]
            [[2, 3], [3, 1]]], # list[tuple[int, int]]
        ],
        [
            [[2, 3]],
            [[1, 2], [3, 1]],
        ],
        [
            [[3, 1], [1, 2]],
            [[2, 3]],
        ],
    ]
    """
