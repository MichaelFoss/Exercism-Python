import re

def get_words(sentence: str) -> list[str]:
    s: str = sentence
    # Ensure commas split
    s = s.replace(',', ', ')
    # Treat underscores like spaces so they split
    s = s.replace('_', ' ')
    # Make all letters lowercase
    s = s.lower()
    # Extract the words
    words: list[str] = s.split()
    return words

def get_word(word: str) -> str:
    alpha_numeric_apostraphe_pattern = r"[a-z0-9']"
    only_word: str = ''
    for (index, ch) in enumerate(word.strip("'")):
        if re.search(alpha_numeric_apostraphe_pattern, ch):
            only_word += ch
    return only_word

def count_words(sentence):
    word_count: dict[str, int] = {}
    words: list[str] = get_words(sentence)
    for word in words:
        stripped_word = get_word(word)
        if len(stripped_word) > 0:
            if stripped_word not in word_count:
                word_count[stripped_word] = 0
            word_count[stripped_word] += 1
    print(str(list(word_count.items())).replace('), ', '),\n'))
    return word_count