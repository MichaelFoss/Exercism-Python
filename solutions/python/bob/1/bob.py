import re

def response(hey_bob: str):
    def contains_letters(s: str):
        for c in s:
            if c.isalpha():
                return True
        return False

    msg = hey_bob.strip()
    has_letters = contains_letters(msg)
    is_silent = len(msg) == 0
    ends_in_question_mark = not is_silent and msg[len(msg) - 1] == '?'
    all_caps = msg.upper() == msg

    if is_silent:
        return 'Fine. Be that way!'

    if all_caps and ends_in_question_mark and has_letters:
        return "Calm down, I know what I'm doing!"

    if ends_in_question_mark:
        return 'Sure.'

    if all_caps and has_letters:
        return 'Whoa, chill out!'

    return 'Whatever.'