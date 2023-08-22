from collections import Counter
from collections.abc import Iterable, Hashable
from typing import TypeVar
from decimal import Decimal
from fractions import Fraction

T = TypeVar('T')
NumberT = TypeVar('NumberT', float, Decimal, Fraction)
HashableT = TypeVar('HashableT', bound=Hashable)


def mode(data: Iterable[NumberT]) -> NumberT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]
