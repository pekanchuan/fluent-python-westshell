from typing import TypeVar, Generic


class Beverage:
    """ 任何饮料 """


class Juice(Beverage):
    """ 任何果汁 """


class OrangeJuice(Juice):
    """ 使用巴西橙子制作的美味果汁 """


T = TypeVar('T')


class BeverageDispenser(Generic[T]):
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """ 安装一个果汁自动售货机 """
