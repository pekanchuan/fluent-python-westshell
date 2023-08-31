from typing import TypedDict


class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int


if __name__ == '__main__':
    pp = BookDict(title='Programming Pearls',
                  authors='Jon Bentley',
                  isbn='0201657880',
                  pagecount=256)

    print(pp)
