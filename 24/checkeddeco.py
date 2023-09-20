"""
>>> @checked
... class Movie:
...     title: str
...     year: int
...     box_office: float
...
>>> movie = Movie(title='The Godfather', year=1972, box_office=137)
>>> movie.title
'The Godfather'
>>> movie
Movie(title='The Godfather', year=1972, box_office=137.0)
"""
from typing import get_type_hints, NoReturn, Any

from checkedlib import Field


def checked(cls: type) -> type:
    for name, constructor in _fields(cls).items():
        setattr(cls, name, Field(name, constructor))

    cls._fields = classmethod(_fields)

    instance_methods = (
        __init__,
        __repr__,
        __setattr__,
        _asdict,
        __flag_unknown_attrs,
    )
    for method in instance_methods:
        setattr(cls, method.__name__, method)

    return cls


def _fields(cls: type) -> dict[str, type]:
    return get_type_hints(cls)


def __init__(self, **kwargs) -> None:
    for name in self._fields():
        value = kwargs.pop(name, ...)
        setattr(self, name, value)
    if kwargs:
        self.__flag_unknown_attrs(*kwargs)


def __setattr__(self, name: str, value) -> None:
    if name in self._fields():
        cls = self.__class__
        descriptor = getattr(cls, name)
        descriptor.__set__(self, value)
    else:
        self.__flag_unknown_attrs(name)


def __flag_unknown_attrs(self, *names: str) -> NoReturn:
    plural = 's' if len(names) > 1 else ''
    extra = ', '.join(f'{name!r}' for name in names)
    cls_name = repr(self.__class__.__name__)
    raise AttributeError(f'{cls_name} object has no attribute{plural} {extra}')


def _asdict(self) -> dict[str, Any]:
    return {
        name: getattr(self, name)
        for name, attr in self.__class__.__dict__.items()
        if isinstance(attr, Field)
    }


def __repr__(self) -> str:
    kwargs = ', '.join(
        f'{key}={value!r}' for key, value in self._asdict().items()
    )
    return f'{self.__class__.__name__}({kwargs})'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
