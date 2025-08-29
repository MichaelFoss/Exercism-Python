"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    if len(vocab_words) == 0:
        raise ValueError('vocab_words must include a prefix')

    prefix = vocab_words[0]
    prefixed_words = [prefix]

    for i in range(1, len(vocab_words)):
        prefixed_words.append(f'{prefix}{vocab_words[i]}')

    return ' :: '.join(prefixed_words)



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    root_word = word[0:-4]
    print(root_word)
    if root_word[-1] == 'i':
        root_word = f'{root_word[0:-1]}y'
    return root_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split(' ')
    if index < 0 and index * -1 > len(words):
        raise IndexError(f'Negative index {index} does not exist in sentence')
    elif index >= 0 and index > len(words) - 1:
        raise IndexError(f'Index {index} does not exist in sentence')

    # If it's a word with punctuation after it, drop the punctuation
    if not words[index][-1].isalpha():
        transformed_word = f'{words[index][0:-1]}en'
    else:
        transformed_word = f'{words[index]}en'

    return transformed_word