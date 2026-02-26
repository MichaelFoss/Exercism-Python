def getIndefiniteArticle(noun: str) -> str:
    if noun == None or len(noun) == 0:
        return 'a'
    if noun[0:1] in 'AEIOUaeiou':
        return 'an'
    return 'a'

def proverb(*nouns: str, **kwargs) -> list[str]:
    if len(nouns) == 0:
        return []
    qualifier: str = f"{kwargs['qualifier']} " if 'qualifier' in kwargs and kwargs['qualifier'] is not None else ''
    lines: list[str] = []
    for i in range(0, len(nouns) - 1):
        formerNoun, latterNoun = nouns[i:i + 2]
        print(formerNoun, latterNoun)
        sentence: str = f'For want of {getIndefiniteArticle(formerNoun)} {formerNoun} the {latterNoun} was lost.'
        lines.append(sentence)
    finalNoun: str = nouns[0]
    indefiniteArticle: str = getIndefiniteArticle(finalNoun) if qualifier == '' else getIndefiniteArticle(qualifier)
    finalSentence: str = f'And all for the want of {indefiniteArticle} {qualifier}{finalNoun}.'
    lines.append(finalSentence)
    return lines
