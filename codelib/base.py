

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

def base16encode(string, layer = 1, upper = False):
    """
    >>> base16encode("string")
    '737472696e67'
    """
    from binascii import hexlify
    if(layer > 0):
        res = base16encode(
                hexlify(string.encode('UTF-8')).decode(),
                layer - 1,
                upper)
        if(upper):
            string = res.upper()
        else:
            string = res
    return string

def base16decode(hex_, layer = 1):
    """
    >>> base16decode('737472696e67')
    'string'
    """
    from binascii import unhexlify
    from string import hexdigits as hex__
    if(layer > 0):
        return base16decode(unhexlify(hex_.lower().encode('UTF-8')).decode(), layer - 1)
    return hex_


