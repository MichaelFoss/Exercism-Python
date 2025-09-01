OPEN_GROUP_CHARACTERS = '[{('
CLOSED_GROUP_CHARACTER_PAIRINGS = {
    ']': '[',
    '}': '{',
    ')': '(',
}

def is_paired(input_string):
    groups: list[str] = []
    for ch in input_string:
        if ch in OPEN_GROUP_CHARACTERS:
            groups.append(ch)
        elif ch in CLOSED_GROUP_CHARACTER_PAIRINGS:
            # Extra closing character (e.g. "[]]")
            if len(groups) == 0:
                return False
            # Mismatched closing character (e.g. "(]")
            last_group_ch = groups.pop()
            if last_group_ch != CLOSED_GROUP_CHARACTER_PAIRINGS[ch]:
                return False

    # Make sure we don't have anything we didn't close
    return len(groups) == 0
