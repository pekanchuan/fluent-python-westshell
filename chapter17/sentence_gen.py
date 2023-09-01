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
        self.words = RE_WORD.findall(text)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == '__main__':
    import doctest
    
    doctest.testmod()