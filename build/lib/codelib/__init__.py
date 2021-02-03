import codelib.rot
import codelib.base

__doc__ = """handy tool for encoding and decoding.



ROT:
───

  (rot13, rot47, rot13CustomIteration, rot47CustomIteration)

  rot13
  ─────

     Form atoz and AtoZ


     >>> rot.rot13(string)           # For both encode & decode.

     >>> rot.rot13IterForword(string, iteration)

     >>> rot.rot13IterBackword(string, iteration)

     >>> rot.rot_char13Forword(char, iteration)

     >>> rot.rot_char13Backword(char, iteration)

  rot47
  ─────

     From atoz , AtoZ , symbols


     >>> rot.rot47(string)           # For both encode & decode.

     >>> rot.rot47IterForword(string, iteration)

     >>> rot.rot47IterBackword(string, iteration)

     >>> rot.rot_char47Forword(char, iteration)

     >>> rot.rot_char47Backword(char, iteration)

BASE:
────

  (base64, hex)

  layer = Number of times encode the encoded value, or decode the decoded value

  base64
  ──────

    >>> base.base64encode(string)

    >>> base.base64decode(base64)

  hex (b16)
  ─────────

    >>> base.hex(string)

    >>> base.unhex(hex)

"""


__all__ = {
        "rot": [
            "rot13",
            "rot47",
            "rot13IterForword",
            "rot13IterBackword",
            "rot47IterForword",
            "rot47IterBackword",
            "rot_char13Forword",
            "rot_char13Backword",
            "rot_char47Forword",
            "rot_char47Backword"
            ],
        "base": [
            "base64encod",
            "base64decode",
            "hex",
            "unhex"
            ]
        }

