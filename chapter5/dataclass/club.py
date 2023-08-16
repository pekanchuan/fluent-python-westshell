from dataclasses import dataclass, field, InitVar


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
    # guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)


# @dataclass
# class C:
#     i: int
#     j: int = None
#     database: InitVar[DatabaseType] = None
#
#     def __post_init__(self, database):
#         if self.j is None and database is not None:
#             self.j = database.lookup('j')
