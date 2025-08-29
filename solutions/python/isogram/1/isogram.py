def is_isogram(string):
    letters = list(string.lower())
    seen_letters = ''
    for char in letters:
        if char.isalpha():
            if char in seen_letters:
                return False
            seen_letters += char
    return True
