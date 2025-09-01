def encode(plain_text):
    encoded_text: str = ''
    for ch in plain_text:
        if len(encoded_text) > 0 and (len(encoded_text) + 1) % 6 == 0:
            encoded_text += ' '
        if ch.isalpha():
            encoded_letter: str = chr(ord(ch.lower()) + 25 - (ord(ch.lower()) - ord('a')) * 2)
            encoded_text += encoded_letter
        elif ch.isdigit():
            encoded_text += ch
    return encoded_text.strip()

def decode(ciphered_text):
    decoded_text: str = ''
    for ch in ciphered_text:
        if ch.isalpha():
            decoded_letter: str = chr(ord(ch.lower()) + 25 - (ord(ch.lower()) - ord('a')) * 2)
            decoded_text += decoded_letter
        elif ch.isdigit():
            decoded_text += ch
    return decoded_text
