"""
>>> word = Text('forward')
>>> word
Text('forward')
>>> word.reverse()
Text('drawrof')
>>> Text.reverse(Text('backward'))
Text('drawkcab')
>>> type(Text.reverse), type(word.reverse)
(<class 'function'>, <class 'method'>)
>>> list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')]))
['diaper', (30, 20, 10), Text('desserts')]
>>> word.reverse
<bound method Text.reverse of Text('forward')>
>>> word.reverse.__self__
Text('forward')
>>> word.reverse.__func__ is Text.reverse
True
"""


import collections


class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()