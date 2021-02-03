

def base64encode(string, layer = 1):
    """
    >>> base64encode('hello')
    'aGVsbG8='
    """
    from binascii import b2a_base64
    if(layer > 0):
        return base64encode(
                b2a_base64(
                    string.encode(
                        'UTF-8')).decode().replace(
                            "\n", ""), layer - 1)
    return string

def base64decode(base64, layer = 1):
    """
    >>> base64decode('aGVsbG8=')
    'hello'
    """
    from binascii import a2b_base64
    if(layer > 0):
        return base64decode(
                a2b_base64(
                    base64.encode(
                        'UTF-8')).decode(), layer - 1)
    return base64

def hex(string, layer = 1):
    from binascii import hexlify
    if(layer > 0):
        return hex(
                hexlify(string.encode('UTF-8')).decode(), layer - 1)
    return string

def unhex(hex_, layer = 1):
    from binascii import unhexlify
    from string import hexdigits as hex__
    if(layer > 0):
        """
        for i in hex_:
            if(i not in tuple(hex__)):
                raise ValueError("Non-hexdecimal charactor found in", hex_)
                """
        return unhex(unhexlify(hex_.encode('UTF-8')).decode(), layer - 1)
    return hex_
