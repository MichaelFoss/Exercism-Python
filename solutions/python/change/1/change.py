"""
Determins the fewest coins given a target to spend them on,
or an empty array if no coins can be found.
"""
def fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    The concept is that we're going to use a double-ended array
    to act as a search list. Each item in the list will have
    a two-dim array, the target and the path achieved to get there.
    The initial search array will only contain a single state,
    the initial target and an empty array (it costs nothing
    to get us to the target amount).

    At the start of the array, we'll remove a potential states
    and for each one we remove we'll split it into all possible new states.
    Each new possible state will be the current target minus
    one coin that goes into it, and we'll add that coin to the path
    used to get there. For every new state, we'll add this to the end
    of the search array.

    During the process of splitting a recently-removed state
    into new states, if the coin we're using is equal to the target,
    we know we've found a path that gets us to the original target.
    At that point, we should stop searching,
    because we've found the answer.

    This approach allows us to create a constantly sorted search array,
    with the shortest lengths of the paths to get to targets at the start.
    This ensures that when we find a path whose target is zero,
    it is an optimal set of coins.

    What is really going on here is a breadth-first search of a tree.
    The root node of the tree is the initial item, with the value
    of the node being the target and empty path. As each item is removed
    from the search array, it is actually marked as "parsed" in the tree,
    and adding new states to the end of the search array essentially adds
    new child nodes to that node in the tree. From a data-structure
    perspective, this is why the first-found path that has a target of 0
    is guaranteed to be the shortest amount of coins – because it is
    the highest up in the tree given that we are using a breadth-first
    search.

    e.g. Target 5, coins [2, 1]:
    // Initialize
    [[5, []]]
    // Remove 5 from start, expand using coins 2 & 1 and place at end
    [[3, [2]], [4, [1]]]
    // Remove 3 from start, expand using coins 2 & 1 and place at end
    [[4, [1]], [1, [2, 2]], [2, [1, 2]]]
    // Remove 4 from start, expand using coins 2 & 1 and place at end
    // Note that we don't add new states if a coin is larger than
    // the lowest coin on the path, as we would end up checking
    // combinations instead of permutations – so in this case,
    // we don't add [2, [2, 1]] because 2 > 1, and we've already got
    // [2, [1, 2]] elsewhere in the search array
    [[1, [2, 2]], [2, [1, 2]], [3, [1, 1]]]
    // Remove 1 from start, stop because it's equal to coin 1
    [0, [1, 2, 2]]
    """

    # Initialize the search array
    search: list[list] = []
    search.append([target, []])
    while len(search) > 0:
        # Remove top-left node from tree
        active_item: list = search.pop(0)
        target: int = active_item[0]
        current_path = active_item[1]
        # Add child nodes to the tree based on all possible coins
        for coin in coins:
            if coin == target:
                result: list[int] = sorted([coin] + current_path.copy())
                return result
            if coin < target and (
                len(current_path) == 0 or
                coin <= current_path[0]
            ):
                new_item = [target - coin, [coin] + current_path.copy()]
                search.append(new_item)
    raise ValueError("can't make target with given coins")


"""
Determines the fewest coins given a target to spend them on,
or raises an error if no set of coins can be found.
"""
def find_fewest_coins(coins, target):
    # Can't make anything without actual currency
    if len(coins) == 0:
        raise ValueError("can't make target with given coins")

    # Or money, for that matter
    if target == 0:
        return []

    # Money has to be positive
    if target < 0:
        raise ValueError("target can't be negative")

    # Unique coins only
    coins = list(set(coins))

    # Sort from highest to lowest
    coins = sorted(coins, reverse=True)

    # If it's exactly one coin, stop here
    if target in coins:
        return [target]

    # Remove all coins bigger than the target
    while True:
        if len(coins) == 0:
            raise ValueError("can't make target with given coins")
        if coins[0] > target:
            coins.remove(coins[0])
        else:
            break

    # Get the fewest coins, if possible
    print(target, coins)
    result: list[int] = fewest_coins(coins, target)
    return result
