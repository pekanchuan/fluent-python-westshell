"""
>>> s = Sentence('"The time has come," the Walrus said,')
>>> s
Sentence('"The time ha... Walrus said,')
>>> for word in s:
...     print(word)
The
time
has
come
the
Walrus
said
>>> list(s)
['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text) -> None:
        self.text = text

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
