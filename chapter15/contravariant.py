from typing import TypeVar, Generic


class Refuse:
    """ 任何废弃物 """


class Biodegradable(Refuse):
    """ 可生物降解的废弃物 """


class Compostable(Biodegradable):
    """ 可制成肥料的废弃物 """


T_contra = TypeVar('T_contra', contravariant=True)


class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        """ 在倾倒前存放垃圾 """


def deploy(trash_can: TrashCan[Biodegradable]):
    """ 放置一个垃圾桶，存放可生物降解的废弃物 """
