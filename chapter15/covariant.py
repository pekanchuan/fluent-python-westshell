from typing import TypeVar, Generic


class Beverage:
    """ 任何饮料 """


class Juice(Beverage):
    """ 任何果汁 """


class OrangeJuice(Juice):
    """ 使用巴西橙子制作的美味果汁 """


# T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)


class BeverageDispenser(Generic[T_co]):
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """ 安装一个果汁自动售货机 """
