import re

class Luhn:
    def __init__(self, card_num):
        self.digits = card_num.replace(" ", "")
        self.is_valid_digits = re.match(r'^([\d]+)$', self.digits)

    def valid(self):
        if not self.is_valid_digits:
            return False
        if len(self.digits) <= 1:
            return False
        reversed_digits = self.digits[::-1]
        sum = 0
        for i in range(0, len(reversed_digits)):
            digit = int(reversed_digits[i])
            if i % 2 == 1:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            sum += digit
        return sum % 10 == 0
        