from typing import Protocol, runtime_checkable
from randompick import RandomPicker


@runtime_checkable
class LoadableRandomPicker(RandomPicker, Protocol):
    def load(self, Iterable) -> None: ...
