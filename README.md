# codelib
python package for encoding and decoding

<a href="https://pypi.python.org/pypi/codelib"><img src="https://img.shields.io/pypi/v/codelib.svg"></a>
<a href="https://pypi.python.org/pypi/codelib"><img src="https://img.shields.io/pypi/l/codelib"></a>
<a href="https://pypi.python.org/pypi/codelib"><img src="https://img.shields.io/pypi/pyversions/codelib.svg"></a>


<b>Installation</b>:

```bash
$ pip install codelib
```

<b>usage</b>:

```python
>>> import codelib
>>> codelib.rot.rot13("hello")
'uryyb'
>>> codelib.rot.rot13('uryyb')
'hello'

>>> codelib.rot.rot47("hello")
'96==@'
>>> codelib.rot.rot47('96==@')
'hello'


>>> codelib.base.base64encode("hello")
'aGVsbG8='
>>> codelib.base.base64decode('aGVsbG8=')
'hello'


>>> codelib.base.base64encode("hellow", 5)
'VjFaV2ExWXlUWGxUYTJoUVVrUkJPUT09'


>>> help(codelib)        # for more Info
```
[⟨More Info⟩](https://madhava-mng.github.io/codelib/)
