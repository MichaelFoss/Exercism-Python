def get_lowercase_alphabet():
    alphabet = ''
    for code in range(97, 97 + 26):
        alphabet += chr(code)
    return alphabet

def is_pangram(sentence):
    '''
    Create a list `letters` of all lowercase letters in the alphabet
    that will be used to track which letter has been seen
    in the sentence. When a letter is seen, make the
    corresponding letter in `letters` uppercase.

    The sentence is a pangram if `letters` is completely uppercase
    by the time the sentence is completely parsed.
    '''
    lowercase_alphabet = get_lowercase_alphabet()
    letters = list(lowercase_alphabet)
    lowercase_sentence = sentence.strip().lower()
    for char in lowercase_sentence:
        if char.isalpha():
            letters[ord(char) - 97] = letters[ord(char) - 97].upper()
    return ''.join(letters) == lowercase_alphabet.upper()