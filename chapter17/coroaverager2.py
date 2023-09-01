from collections.abc import Generator
from typing import Union, NamedTuple, TypeAlias


class Result(NamedTuple):
    count: int
    average: float


class Sentinel:
    def __repr__(self) -> str:
        return f'<Sentinel>'


STOP = Sentinel()

# SendType = Union[float, Sentinel]
SendType: TypeAlias = float | Sentinel


def averager2(verbose: bool = False) -> Generator[None, float | Sentinel, Result]:
    total = 0.0
    count = 0.0
    average = 0.0
    while True:
        term = yield average
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


if __name__ == '__main__':
    # coro_avg = averager2()
    # next(coro_avg)
    # coro_avg.send(10)
    # coro_avg.send(30)
    # coro_avg.send(6.5)
    # try:
    #     coro_avg.send(STOP)
    # except StopIteration as exc:
    #     result = exc.value

    # print(result)

    def compute():
        res = yield from averager2(True)
        print("computed:", res)
        return res

    comp = compute()
    for v in [None, 10, 20, 30, STOP]:
        try:
            comp.send(v)
        except StopIteration as exc:
            result = exc.value

    print(result)
