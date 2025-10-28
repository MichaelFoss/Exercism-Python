def transpose(text):
    if text == None or text == '':
        return ''
    lines: list[str] = text.split('\n')
    maxLength: int = len(max(lines, key=len))
    newLines: list[str] = [''] * maxLength
    for rowIndex, line in enumerate(lines):
        for columnIndex in range(0, len(line)):
            letter: str = line[columnIndex]
            newLines[columnIndex] += (rowIndex - len(newLines[columnIndex])) * ' '
            newLines[columnIndex] += letter
    return '\n'.join(newLines)
