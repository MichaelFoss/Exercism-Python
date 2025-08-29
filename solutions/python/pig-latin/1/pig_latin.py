VOWELS = ['a', 'e', 'i', 'o', 'u']

def get_word_parts(s: str):
    text = s.lower()

    for c in VOWELS + ['xr', 'yt']:
        if text.startswith(c):
            return {
                'beginningConsonants': '',
                'startsWithVowelOrXROrYT': True,
                'endsBeginningWithQU': False,
                'endsBeginningWithY': False,
            }

    word = text
    parts = {
                'beginningConsonants': '',
                'startsWithVowelOrXROrYT': False,
                'endsBeginningWithQU': False,
                'endsBeginningWithY': False,
            }
    index = 0
    while parts['beginningConsonants'] == '' and not parts['endsBeginningWithQU'] and not parts['endsBeginningWithY']:
        if word[index] in VOWELS:
            if index != 0 and word[index - 1] == 'q' and word[index] == 'u':
                if index == 1:
                    parts['beginningConsonants'] = ''
                else:
                    parts['beginningConsonants'] = word[0:index - 1]
                parts['endsBeginningWithQU'] = True
            else:
                parts['beginningConsonants'] = s[0:index]
        elif word[index] == 'y':
            if index == 0:
                parts['beginningConsonants'] = ''
            else:
                parts['beginningConsonants'] = word[0:index]
                parts['endsBeginningWithY'] = True
        index += 1
        if parts['beginningConsonants'] == '' and index == len(word):
            parts['beginningConsonants'] = word
    return parts

def translate_word(text):
    text = text.strip()
    if len(text) == 0:
        return ''

    parts = get_word_parts(text)

    print(parts)

    if parts['startsWithVowelOrXROrYT']:
        return text + 'ay'

    if parts['endsBeginningWithQU']:
        return (
            text[len(parts['beginningConsonants']) + 2:len(text)]
            + parts['beginningConsonants']
            + 'qu'
            + 'ay'
        )

    if parts['endsBeginningWithY']:
        return (
            'y'
            + text[len(parts['beginningConsonants']) + 1:len(text)]
            + parts['beginningConsonants']
            + 'ay'
        )

    if len(parts['beginningConsonants']) == '':
        return (
            text
            + 'ay'
        )

    return (
        text[len(parts['beginningConsonants']):len(text)]
        + parts['beginningConsonants']
        + 'ay'
    )

    raise RuntimeError(f'Unhandled case for word {text}')

def translate(text):
    phrase = text.split()

    if len(phrase) == 0:
        return ''

    pig_latin_phrase = ''

    for word in phrase:
        pig_latin_word = translate_word(word)
        if pig_latin_phrase != '':
            pig_latin_phrase += ' '
        pig_latin_phrase += pig_latin_word

    return pig_latin_phrase