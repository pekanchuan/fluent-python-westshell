import collections


def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, item):
        return super().__contains__(_upper(item))


class UpperDict(UpperCaseMixin, collections.UserDict):
    pass


class UpperCounter(UpperCaseMixin, collections.Counter):
    """一个特俗的计数器，字符串键是大写形式"""
