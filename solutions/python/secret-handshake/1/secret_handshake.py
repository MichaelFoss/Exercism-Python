ACTIONS: list[str] = [
    'wink',
    'double blink',
    'close your eyes',
    'jump',
]
EXECUTE_ACTION: str = '1'
VALID_CHARACTERS: str = '01'

def commands(binary_str: str) -> str:
    # Make sure it's valid
    if len(binary_str) != 5:
        raise ValueError('binary_str must be exactly 5 characters')
    binary_set: set[str] = set(binary_str)
    if not binary_set.issubset(VALID_CHARACTERS):
        raise ValueError('binary_str must only contain ["1", "0"]')

    # Iterate over binary_str, starting at the end
    # and stopping just before the first flag
    executed_actions: list[str] = []
    action_flags: list[str] = binary_str[::-1][:-1]
    for action_index, action_flag in enumerate(action_flags):
        if action_flag == EXECUTE_ACTION:
            executed_actions.append(ACTIONS[action_index])

    # If the first flag is set, reverse the action order
    is_reversed: bool = binary_str[0:1] == EXECUTE_ACTION
    if is_reversed:
        executed_actions.reverse()

    return executed_actions
