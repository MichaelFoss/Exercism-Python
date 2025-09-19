# subclassing the Exception to create a StackUnderflowError
class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

# "ASM"-level commands
POP_AX = 'pop_ax'
POP_BX = 'pop_bx'
PUSH_AX = 'push_ax'
PUSH_BX = 'push_bx'
REG_ADD = 'reg_add'
REG_SUB = 'reg_sub'
REG_MUL = 'reg_mul'
REG_DIV = 'reg_div'

def pop_ax(stack: list[int], registers: list[int]) -> None:
    if len(stack) == 0:
        raise StackUnderflowError('Insufficient number of items in stack')
    registers[0] = stack.pop()

def pop_bx(stack: list[int], registers: list[int]) -> None:
    if len(stack) == 0:
        raise StackUnderflowError('Insufficient number of items in stack')
    registers[1] = stack.pop()

def push(stack: list[int], val: int) -> None:
    stack.append(val)

def push_ax(stack: list[int], registers: list[int]) -> None:
    stack.append(registers[0])

def push_bx(stack: list[int], registers: list[int]) -> None:
    stack.append(registers[1])

def reg_add(registers: list[int]) -> int:
    registers[0] = registers[0] + registers[1]

def reg_sub(registers: list[int]) -> int:
    registers[0] = registers[0] - registers[1]

def reg_mul(registers: list[int]) -> int:
    registers[0] = registers[0] * registers[1]

def reg_div(registers: list[int]) -> int:
    if registers[1] == 0:
        raise ZeroDivisionError('divide by zero')
    registers[0] = registers[0] // registers[1]

def get_initial_words() -> dict[str, list]:
    return {
        '+': [POP_BX, POP_AX, REG_ADD, PUSH_AX],
        '-': [POP_BX, POP_AX, REG_SUB, PUSH_AX],
        '*': [POP_BX, POP_AX, REG_MUL, PUSH_AX],
        '/': [POP_BX, POP_AX, REG_DIV, PUSH_AX],
        # [a] -> [a, a]
        'DUP': [POP_AX, PUSH_AX, PUSH_AX],
        # [a, b] -> [a]
        'DROP': [POP_AX],
        # [a, b] -> [b, a]
        'SWAP': [POP_AX, POP_BX, PUSH_AX, PUSH_BX],
        # [a, b] -> [a, b, a]
        'OVER': [POP_AX, POP_BX, PUSH_BX, PUSH_AX, PUSH_BX],
    }


def get_initial_registers() -> list[int]:
    """
    Returns ax=0, bx=0 in a list of len 2.
    """
    return [0, 0]


def add_additional_words(words: dict[str, list], new_word_lines: list[str]) -> None:
    for new_word_line in new_word_lines:
        if new_word_line[0] != ':' or new_word_line[-1] != ';':
            raise ValueError('undefined operation')
        parts: list[str] = new_word_line.upper()[1:-1].split()
        new_word: str = parts[0]
        if is_int(new_word):
            raise ValueError('illegal operation')
        commands: list[str] = parts[1:]
        # Create a new command list
        new_word_commands: list = []
        # For every command in the command,
        # add the commands to the word's command
        for command in commands:
            if is_int(command):
                new_word_commands += [int(command)]
            else:
                if command not in words:
                    raise ValueError('undefined operation')
                new_word_commands += words[command].copy()
        words[new_word] = new_word_commands


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def execute_word(word: str, words: dict[str, list[str]], stack: list[int], registers: list[int]) -> None:
    for command in words[word]:
        if is_int(command):
            push(stack, int(command))
        elif command == POP_AX:
            pop_ax(stack, registers)
        elif command == POP_BX:
            pop_bx(stack, registers)
        elif command == PUSH_AX:
            push_ax(stack, registers)
        elif command == PUSH_BX:
            push_bx(stack, registers)
        elif command == REG_ADD:
            reg_add(registers)
        elif command == REG_SUB:
            reg_sub(registers)
        elif command == REG_MUL:
            reg_mul(registers)
        elif command == REG_DIV:
            reg_div(registers)
        else:
            raise ValueError('undefined operation')
        

def evaluate(input_data: list[str]) -> list[int]:
    registers: list[int] = get_initial_registers()
    words: dict[str, list[str]] = get_initial_words()
    add_additional_words(words, input_data[0:-1])
    stack: list[int] = []
    program: list[str] = input_data[-1].upper().split()
    if program[0] == ':' or program[-1] == ';':
        raise ValueError('illegal operation')

    # Program uses two temporary storage variables, ax & bx
    # Program can also use operations push_ax, pop_ax, push_bx, pop_bx
    # 
    # 1. Add base words
    # 2. Parse new words and add them as operations
    # 3. Tokenize program – split string into words and numbers
    # 4. Run program

    for token in program:
        if is_int(token):
            val: int = int(token)
            stack.append(val)
        else:
            word: str = token
            if word not in words:
                raise ValueError('undefined operation')
            execute_word(word, words, stack, registers)
    return stack
