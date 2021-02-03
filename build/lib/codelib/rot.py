
def rot_char13Forword(char, rotate):
    char_place = ord(char)
    # uppper handling.
    if(char_place < 91 and char_place > 64):
        for i in range(rotate):
            char_place += 1
            if(char_place >= 91):
                char_place = 65
        return chr(char_place)
    # Lower handling.
    if(char_place < 123 and char_place > 96):
        for i in range(rotate):
            char_place += 1
            if(char_place >= 123):
                char_place = 97
        return chr(char_place)
    # just return the arg
    return char

def rot_char13Backword(char, rotate):
    char_place = ord(char)
    # Upper handling.
    if(char_place < 91 and char_place > 64):
        for i in range(rotate):
            char_place -= 1
            if(char_place <= 64):
                char_place = 90
        return chr(char_place)
    # Lower handling.
    if(char_place < 123 and char_place > 96):
        for i in range(rotate):
            char_place -= 1
            if(char_place <= 96):
                char_place = 122
        return chr(char_place)
    # just return arg.
    return char


def rot13(string):
    """
    >>> rot13('uryyb')
    'hello'
    >>> rot13('hello')
    'uryyb'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char13Forword(i, 13)
    return tmp_string

def rot13IterForword(string, rotate):
    """
    >>> rot13IterForword('abc', 1)
    'bcd'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char13Forword(i, rotate)
    return tmp_string

def rot13IterBackword(string, rotate):
    """
    >>> rot13IterBackword('abc', 1)
    'zab'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char13Backword(i, rotate)
    return tmp_string

def rot_char47Forword(char, rotate):
    char_place = ord(char)
    if(char_place < 127 and char_place > 32):
        for i in range(rotate):
            char_place += 1
            if(char_place >= 127):
                char_place = 33
        return chr(char_place)
    return char

def rot_char47Backword(char, rotate):
    char_place = ord(char)
    if(char_place < 127 and char_place > 32):
        for i in range(rotate):
            char_place -= 1
            if(char_place <= 32):
                char_place = 126
        return chr(char_place)
    return char

def rot47(string):
    """
    >>> rot47encode('hello')
    '96==@'
    >>> rot47decode('96==@')
    'hello'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char47Forword(i, 47)
    return tmp_string


def rot47IterForword(string, rotate):
    """
    >>> rot47IterForword('ABC', 1)
    'BDC'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char47Forword(i, rotate)
    return tmp_string

def rot47IterBackword(string, rotate):
    """
    >>> rot47IterBackword('BDC', 1)
    'ABC'
    """
    tmp_string = ""
    for i in string:
        tmp_string += rot_char47Backword(i, rotate)
    return tmp_string
