LOWERCASE_Z_ORD = ord('z')

def rotate(text: str, key: int):
    # Normalize the key so it is between 0 and 25
    if key < 0:
        while key < 0:
            key += 26
    if key > 26:
        while key > 26:
            key -= 26

    # Translate the text
    cipher = ''
    for ch in text:
        if ch.isalpha():
            is_uppercase_letter = ch.upper() == ch
            ch_code = ord(ch.lower())
            ch_code += key
            if ch_code > LOWERCASE_Z_ORD:
                ch_code -= 26
            new_ch = chr(ch_code)
            if is_uppercase_letter:
                new_ch = new_ch.upper()
            cipher += new_ch
        else:
            cipher += ch
    return cipher
